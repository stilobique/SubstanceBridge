# ##### Substance Bridge #####
# A simple bridge between painter and blender.
#
# Thx Jerem.

# -----------------------------------------------------------------------------
# Import all Package addon
# -----------------------------------------------------------------------------
import sys
import importlib

from . import addon_updater_ops

modulesNames = [
    'config.settings',
    # Models
    'models.paths',
    'models.project',
    # Views
    'views.SubstanceProject',
    'views.TextureSetList',
    # 'views.Baking',
    'views.MoresOpt',
    'views.DataView',
    # Controllers
    'controllers.SubstanceCheck',
    'controllers.SubstancePainter',
    'controllers.SubstanceController',
    'controllers.SubstanceSetup',
    'controllers.DebugOps',
    # Auto Updater
    'addon_updater',
    'addon_updater_ops',
    ]

modulesFullNames = []
for currentModule in modulesNames:
    modulesFullNames.append('{}.{}'.format(__name__, currentModule))

for currentModule in modulesFullNames:
    if currentModule in sys.modules:
        importlib.reload(sys.modules[currentModule])
    else:
        globals()[currentModule] = importlib.import_module(currentModule)


# -----------------------------------------------------------------------------
# MetaData Add-On Blender
# -----------------------------------------------------------------------------
bl_info = {
    "name": "Substance Bridge",
    "author": "stilobique",
    "version": (0, 5, 5),
    "blender": (2, 78),
    "location": "Tool Shelf > Substance Panel",
    "description": "A simple way to export into substance painter.",
    "warning": "",
    "wiki_url": "https://github.com/stilobique/SubstanceBridge/wiki",
    "category": "3D View",
    "tracker_url": "https://github.com/stilobique/SubstanceBridge/issues",
}


# -----------------------------------------------------------------------------
# Update register all methods to this addons
# -----------------------------------------------------------------------------
def register():
    # Check the number version Addon
    addon_updater_ops.check(bl_info)

    # Add all class present in this addon
    for module in modulesFullNames:
        if module in sys.modules:
            if hasattr(sys.modules[module], 'register'):
                sys.modules[module].register()


# -----------------------------------------------------------------------------
# Delete register
# -----------------------------------------------------------------------------
def unregister():
    for module in modulesFullNames:
        if module in sys.modules:
            if hasattr(sys.modules[module], 'unregister'):
                sys.modules[module].unregister()
