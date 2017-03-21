import bpy

from bpy.props import *


# ----------------------------------------------------------------------------
# Model to define all path and settings :
#  -> Substance Painter Path
# ----------------------------------------------------------------------------
class SbsModelsSetup(bpy.types.PropertyGroup):
    path_designer = StringProperty(
            name="Substance Designer",
            subtype='FILE_PATH',
            )
    path_batchtools = StringProperty(
            name="Batch Tools",
            subtype='DIR_PATH',
            )
    path_shelf_sbs = StringProperty(
            name="Shelf SBS",
            subtype='DIR_PATH',
            )


def register():
    bpy.utils.register_class(SbsModelsSetup)
    bpy.types.Scene.sbs_path_settings = \
        bpy.props.PointerProperty(type=SbsModelsSetup)


def unregister():
    bpy.utils.unregister_class(SbsModelsSetup)
    del bpy.types.Scene.sbs_path_settings
