# ##### Substance Bridge #####
# A simple bridge between painter and blender.
#
# Thx Jerem.

# -----------------------------------------------------------------------------
# Import all Package addon
# -----------------------------------------------------------------------------
modulesNames = [
    'settings',
    'controllers.SubstancePainter',
    'views.GUI']

modulesFullNames = []
for currentModuleName in modulesNames:
    modulesFullNames.append('{}.{}'.format(__name__, currentModuleName))

import bpy
import sys
import importlib

for currentModuleName in modulesFullNames:
    if currentModuleName in sys.modules:
        importlib.reload(sys.modules[currentModuleName])
    else:
        globals()[currentModuleName] = importlib.import_module(currentModuleName)


# -----------------------------------------------------------------------------
# MetaData Add-On Blender
# -----------------------------------------------------------------------------
bl_info = {
    "name": "Substance Bridge",
    "author": "stilobique",
    "version": (0, 3, 1),
    "blender": (2, 78),
    "location": "Tool Shelf > Substance Panel",
    "description": "A simple way to export into substance painter.",
    "warning": "",
    "wiki_url": "",
    "category": "3D View"
}


# -----------------------------------------------------------------------------
# Settings for this addons
# -----------------------------------------------------------------------------
class SubstanceVariable(bpy.types.PropertyGroup):
    # Temporary Folder and obj mesh
    tmp_folder = bpy.context.user_preferences.filepaths.temporary_directory
    mesh_name = 'tmp.obj'
    tmp_mesh = tmp_folder + mesh_name

    # bpy.types.Scene.ProjectName = bpy.props.StringProperty(
    #     name="Project")
    # scn['ProjectName'] = "Painter Project"


# -----------------------------------------------------------------------------
# Update register all methods to this addons
# -----------------------------------------------------------------------------
def register():
    for currentModuleName in modulesFullNames:
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'register'):
                sys.modules[currentModuleName].register()

    bpy.types.Scene.sppfile = bpy.props.StringProperty(
        name="Project Path",
        default="",
        description="Field project path",
        subtype='FILE_PATH'
    )
    bpy.utils.register_class(SubstanceVariable)


# -----------------------------------------------------------------------------
# Delete register
# -----------------------------------------------------------------------------
def unregister():
    for currentModuleName in modulesFullNames:
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'unregister'):
                sys.modules[currentModuleName].unregister()
    bpy.utils.unregister_class(SubstanceVariable)
