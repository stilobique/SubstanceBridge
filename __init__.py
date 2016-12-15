# ##### Substance Bridge #####
# A simple bridge between painter and blender.
#
# Thx Jerem.

# -----------------------------------------------------------------------------
# Import all Package addon
# -----------------------------------------------------------------------------
import bpy

from SubstanceBridge.settings import SubstanceSettings
from SubstanceBridge.controllers.SubstancePainter import Send_to_painter
# from SubstanceBridge.controllers.SubstanceBatchTools import BatchTools
# from SubstanceBridge.views.GUI import SubstanceProjectPanel,
# TextureSetListPanel, BakingSubstancePanel
from SubstanceBridge.views.GUI import *

# -----------------------------------------------------------------------------
# MetaData Add-On Blender
# -----------------------------------------------------------------------------
bl_info = {
    "name": "Substance Bridge",
    "author": "stilobique",
    "version": (0, 3, 1),
    "blender": (2, 78, 1),
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


# -----------------------------------------------------------------------------
# Update register all methods to this addons
# -----------------------------------------------------------------------------
def register():
    bpy.utils.register_class(Send_to_painter)
    # GUI class
    bpy.utils.register_class(SubstanceProjectPanel)
    bpy.utils.register_class(TextureSetListPanel)
    bpy.utils.register_class(BakingSubstancePanel)
    bpy.utils.register_class(SubstanceSettings)
    bpy.utils.register_class(SubstanceVariable)
    bpy.types.Scene.sppfile = bpy.props.StringProperty(
        name="Project Path",
        default="",
        description="Field project path",
        subtype='FILE_PATH'
        )


# -----------------------------------------------------------------------------
# Delete register
# -----------------------------------------------------------------------------
def unregister():
    bpy.utils.unregister_class(Send_to_painter)
    # GUI class
    bpy.utils.unregister_class(SubstanceProjectPanel)
    bpy.utils.unregister_class(TextureSetListPanel)
    bpy.utils.unregister_class(BakingSubstancePanel)
    bpy.utils.unregister_class(SubstanceSettings)
    bpy.utils.unregister_class(SubstanceVariable)


if __name__ == "__main__":
    register()
