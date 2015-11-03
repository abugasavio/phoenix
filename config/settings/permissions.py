# create the smartmin CRUDL permissions on all objects
PERMISSIONS = {'*': ('create', # can create an object
                     'read',   # can read an object, viewing it's details
                     'update', # can update an object
                     'delete', # can delete an object,
                     'list'),  # can view a list of the objects
               'animals.animal': ('add_offspring',),
               }

# GROUPS
GROUP_LOGGED_IN = 'logged in'
GROUP_MANAGE_ACCOUNT = 'manage account'
GROUP_MANAGE_LIVESTOCK = 'manage livestock'
GROUP_MANAGE_PRODUCTION = 'manage production'


GROUP_PERMISSIONS = {
    GROUP_LOGGED_IN: ('animals.animal_list', 'animals.animal_read', 'services.service_list', 'services.service_read',
                      'health.treatment_read', 'health.treatment_list', 'notes.note_list', 'notes.note_read',
                      'services.service_read', 'services.service_list', 'categories.category_list', 'categories.category_read',
                      'animals.pregnancycheck_read', 'animals.pregnancycheck_list',
                      'animals.milkproduction_read', 'animals.milkproduction_list',
                      'animals.lactationperiod_read', 'animals.lactationperiod_list',
                      'auth.user_list', 'auth.user_read', 'groups.group_read', 'groups.group_list',
                      # sires and dams
                      'animals.sire_list', 'animals.dam_list', 'animals.sire_read', 'animals.dam_read',
                      # breeder
                      'animals.breeder_list', 'animals.breeder_read',
                      ),

    GROUP_MANAGE_LIVESTOCK: ('animals.animal_create', 'animals.animal_update', 'animals.animal_delete', 'animals.animals_add_offspring',
                             'groups.group_create', 'groups.group_update', 'groups.group_delete',
                             'health.treatment_create', 'health.treatment_delete', 'health.treatment_update',
                             'notes.note_create', 'notes.note_update', 'notes.note_delete',
                             # sire and dams
                             'animals.sire_create', 'animals.sire_update', 'animals.dam_create', 'animals.dam_update',
                             # breeder
                             'animals.breeder_create', 'animals.breeder_update',
                             ),

    GROUP_MANAGE_ACCOUNT: ('auth.user_create', 'auth.user_delete', 'auth.user_update',),

    GROUP_MANAGE_PRODUCTION: ('services.service_create', 'services.service_update', 'services.service_delete',
                              'animals.pregnancycheck_create', 'animals.pregnancycheck_update', 'animals.pregnancycheck_delete',
                              'animals.milkproduction_create', 'animals.milkproduction_update', 'animals.milkproduction_delete',
                              'animals.lactationperiod_create', 'animals.lactationperiod_update', 'animals.lactationperiod_delete',
                              ),
}