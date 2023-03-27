PLUGIN_NAME = 'Clockss Plugin'
DESCRIPTION = 'CLOCKSS preservation plugin'
AUTHOR = 'Andy Byers'
VERSION = '1.1'
SHORT_NAME = 'clockss'
MANAGER_URL = None
JANEWAY_VERSION = "1.5.0"

from utils import models


def install():
    new_plugin, created = models.Plugin.objects.get_or_create(name=SHORT_NAME, version=VERSION, enabled=True)

    if created:
        print('Plugin {0} installed.'.format(PLUGIN_NAME))
    else:
        print('Plugin {0} is already installed.'.format(PLUGIN_NAME))


def hook_registry():
    # On site load, the load function is run for each installed plugin to generate
    # a list of hooks.
    pass
