from fabric.api import local


def prepare_deploy():
    local("py.test phoenix")
    local("git add -p && git commit")
    local("git push")