import bpy

from bpy.props import *


# ----------------------------------------------------------------------------
# Class for all settings
# ----------------------------------------------------------------------------
class SubstanceProjectItems(bpy.types.PropertyGroup):
    # Name of Substance Project
    prj_name = bpy.props.StringProperty(
        name="Project Name",
        default="Sbs Project",
        )
    # Path File to edit this project
    path_spp = StringProperty(
        name="Project Path",
        default="C:/",
        description="Field project path",
        subtype='FILE_PATH'
    )
    # List of mesh
    meshs_name = []

    # List of Texture Set
    tx_set_index = StringProperty(
        name="Name Set",
        default="Default",
        )


# ----------------------------------------------------------------------------
# Texture Set List Collection
# ----------------------------------------------------------------------------
class TextureSetListItems(bpy.types.PropertyGroup):
    id = IntProperty(
        name="ID Texture Set List",
        default=0,
        )
    name = StringProperty(
        name="Name Set",
        default="Default",
        )
    meshs = StringProperty(
        name="Name Set",
        default="Default",
        )


def register():
    bpy.utils.register_class(SubstanceProjectItems)
    bpy.types.Scene.sbs_project_settings = \
        bpy.props.PointerProperty(type=SubstanceProjectItems)
    # Nominate project variable
    bpy.types.Scene.sppfile = StringProperty(
        name="Project Path",
        default="",
        description="Field project path",
        subtype='FILE_PATH'
    )
    # Nominate texture set variable
    bpy.utils.register_class(TextureSetListItems)
    bpy.types.Scene.tx_set_settings = \
        bpy.props.CollectionProperty(type=TextureSetListItems)


def unregister():
    # Nominate project variable
    del bpy.types.Scene.sbs_project_settings
    del bpy.types.Scene.sppfile
    # Nominate texture set variable
    del bpy.types.Scene.tx_set_list
