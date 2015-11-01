from fabric.api import env, cd, sudo, prefix, prompt, local, get, put
from contextlib import contextmanager as _contextmanager
from fabric.contrib.console import confirm
from fabric.contrib.files import exists
import ntpath
from fabric.utils import abort


env.directory = '/opt/webapps/phoenixenv/'
env.activate = 'source /opt/webapps/phoenixenv/bin/activate'

# Custom
env.deploy_dir = env.directory + 'project-phoenix'
env.deploy_dir_temp_bak = env.directory + 'project-phoenix-temp-bak'


@_contextmanager
def virtualenv():
    with cd(env.directory):
        # Activate env
        with prefix(env.activate):
            yield


def staging():
    env.user = 'ubuntu'
    env.hosts = ['staging.farmguru.co']


def prod():
    env.user = 'ubuntu'
    env.hosts = ['app.farmguru.co']


def is_staging():
    return 'staging.farmguru.co' in env.hosts


def is_production():
    return 'app.farmguru.co' in env.hosts


def confirm_production_backups():
    if not confirm("Have you created an RDS snapshot?"):
        return False

    if not confirm("Have exited all virtualenv sessions?"):
        return False

    return True


def backup_deploy_dir():
    if exists(env.deploy_dir):
        create_local_backup(env.deploy_dir)

        # Rename to a backup
        if exists(env.deploy_dir_temp_bak):
            sudo('rm -rf ' + env.deploy_dir_temp_bak)
        sudo('mv ' + env.deploy_dir + ' ' + env.deploy_dir_temp_bak)


        sudo('mkdir ' + env.deploy_dir)
    else:
        sudo('mkdir ' + env.deploy_dir)


def empty_deploy_dir():
    if exists(env.deploy_dir):
        # Delete
        sudo('rm -r ' + env.deploy_dir)
        # Recreate empty
        sudo('mkdir ' + env.deploy_dir)
    else:
        sudo('mkdir ' + env.deploy_dir)


def delete_deploy_dir_pyc_files():
    with cd(env.deploy_dir):
        # Delete .pyc files
        sudo('find . -name "*.pyc" -exec rm -rf {} \;')


def download_source_code():
    # Ask for tag to clone
    tag = prompt("What tag/branch do you want to pull?")

    with cd(env.deploy_dir):
        try:
            if not exists(env.deploy_dir + "/.git"):
                # Clone repository
                sudo("git clone https://savioabuga@bitbucket.org/savioabuga/farmguru.git %s" % env.deploy_dir)
                sudo("git checkout " + tag)
            else:
                sudo("git pull && git checkout " + tag)
        except SystemExit:
            print "Try again."
            download_source_code()


def create_local_py():
    # Make sure settings/local.py points to staging.py or prod.py
    with cd(env.deploy_dir):
        if is_production():
            sudo('echo "from config.settings.production import *" > config/settings/local.py')
        elif is_staging():
            sudo('echo "from config.settings.staging import *" > config/settings/local.py')
        else:
            abort("Unable to update settings/local.py - unable to determine environment.")


def edit_env_file():
    with cd(env.deploy_dir):
        edit_file(env.deploy_dir_temp_bak + "/config/settings/.env", ".env-temp", env.deploy_dir + "/config/settings/.env")


def install_requirements():
    with cd(env.deploy_dir):
        if is_production():
            sudo('pip install -r requirements/production.txt')
        elif is_staging():
            sudo('pip install -r requirements/local.txt')
        else:
            abort("Unable to install requirements - unable to determine environment.")


def deploy():
    # Enter virtual env
    with virtualenv():
        # Attempt to stop services
        stop_services()

        if is_production() and not confirm_production_backups():
            print "Please perform backups."
            return

        # Backups
        if confirm("Backup deploy dir?"):
            backup_deploy_dir()

    # Leave virtual env to see if we'd like to launch explorer (or finder) with the local directory
    # If you don't leave virtualenv, it affects local() too and returns a 'path not found' error
    if confirm("Open local directory to view backup?"):
        local('open ./')

    # Enter virtual env
    with virtualenv():
        if confirm("Empty deploy dir?"):
            empty_deploy_dir()

        if confirm("Delete .pyc files from deploy dir?"):
            delete_deploy_dir_pyc_files()

        # Download source code
        if confirm("Download source code?"):
            download_source_code()

        # Create local.py
        if confirm("Create local.py?"):
            create_local_py()

        # Edit settings file
        if confirm("Edit env file?"):
            edit_env_file()

        # Install requirements
        if confirm("Install requirements?"):
            install_requirements()

        with cd(env.deploy_dir):
            # Syncdb
            if confirm("Syncdb?"):
                sudo('python manage.py syncdb')

            # Migrate
            if confirm("Migrate?"):
                sudo('python manage.py migrate')

            # Collect static
            if confirm("Collectstatic?"):
                sudo('python manage.py collectstatic')

        start_services()

    # Delete local temp files
    delete_local_temp_files()


def stop_services():
    if confirm("Stop nginx?"):
        sudo('service nginx stop')

    if confirm("Stop supervisord?"):
        # Stop supervisord and all the rest
        sudo('supervisorctl stop all')


def start_services():
    if confirm("Start nginx?"):
        sudo('service nginx start')

    if confirm("Start supervisord?"):
        sudo('service supervisor restart')  # Restart, to make sure the config is reloaded

        # Also ensure all services are started
        sudo('supervisorctl start all')


def create_local_backup(filepath):
    directory = ntpath.dirname(filepath)
    filename = ntpath.basename(filepath)
    backupfile = "%s.tar.gz" % filename
    with cd(directory):
        sudo("tar -zcf %s %s" % (backupfile, filename))
        get(backupfile, backupfile)


def edit_file(remote_path, local_file, final_destination_path):
    get(remote_path, local_file)
    print('File has been downloaded to: ' + local_file + '. Edit it and save.')
    if confirm("Done editing?"):
        put(local_file, final_destination_path, use_sudo=True)
        mark_for_local_deletion(local_file)


def mark_for_local_deletion(filepath):
    if not hasattr(env, 'local_delete_files'):
        env.local_delete_files = []
    env.local_delete_files.append(filepath)


def delete_local_temp_files():
    if hasattr(env, 'local_delete_files') and env.local_delete_files:
        for filename in env.local_delete_files:
            if confirm("Delete local temp file: " + filename + "?"):
                local("rm " + filename)
