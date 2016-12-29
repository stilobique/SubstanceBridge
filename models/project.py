# Project Substance
#  -> Name -> String
#  -> Path .sppfile
#  -> Mesh(s)
#       -> furnitur (example)
#       -> drawers right (example)
#       -> drawers left (example)
#   -> Texture Set List
#       -> furnitur (material)
#       -> drawers (material)

import bpy

from bpy.props import *


# ----------------------------------------------------------------------------
# Class for all settings
# ----------------------------------------------------------------------------
class SubstanceProjectItems(bpy.types.PropertyGroup):
    # Name of Substance Project
    # project_name = StringProperty(
    #     name="Project Name",
    #     default="Default",
    #     )
    # Path File to edit this project
    path_spp = StringProperty(
        name="Project Path",
        default="C:/",
        description="Field project path",
        subtype='FILE_PATH'
    )
    # List of mesh
    meshs_index = StringProperty(
        name="Name Set",
        default="Default",
        )
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
    bpy.types.Scene.project_settings = \
        bpy.props.CollectionProperty(type=SubstanceProjectItems)
    # Nominate project variable
    bpy.types.Scene.project_name = \
        StringProperty(default="substance project")
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
    del bpy.types.Scene.project_settings
    del bpy.types.Scene.project_name
    del bpy.types.Scene.sppfile
    # Nominate texture set variable
    del bpy.types.Scene.tx_set_list
