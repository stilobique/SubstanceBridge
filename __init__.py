# ##### Substance Bridge #####
# A simple bridge between painter and blender.
#
# Thx Jerem.

# -----------------------------------------------------------------------------
# Import all Package addon
# -----------------------------------------------------------------------------
import bpy
import sys
import importlib

modulesNames = [
    'config.settings',
    # Models
    'models.project',
    # Views
    'views.SubstanceProject',
    # 'views.TextureSetList',
    'views.Baking',
    'views.DebugPanel',
    'views.DataView',
    # Controllers
    'controllers.SubstancePainter',
    'controllers.SubstanceController',
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
    "version": (0, 4, 1),
    "blender": (2, 78),
    "location": "Tool Shelf > Substance Panel",
    "description": "A simple way to export into substance painter.",
    "warning": "",
    "wiki_url": "https://github.com/stilobique/SubstanceBridge/wiki",
    "category": "3D View",
    "tracker_url": "https://github.com/stilobique/SubstanceBridge/issues"
}


# -----------------------------------------------------------------------------
# Update register all methods to this addons
# -----------------------------------------------------------------------------
def register():
    for currentModule in modulesFullNames:
        if currentModule in sys.modules:
            if hasattr(sys.modules[currentModule], 'register'):
                sys.modules[currentModule].register()


# -----------------------------------------------------------------------------
# Delete register
# -----------------------------------------------------------------------------
def unregister():
    for currentModule in modulesFullNames:
        if currentModule in sys.modules:
            if hasattr(sys.modules[currentModule], 'unregister'):
                sys.modules[currentModule].unregister()
