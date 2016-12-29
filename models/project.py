# Project Substance
#  -> Name -> String
#  -> Path .sppfile
#  -> Mesh(s)
#       -> furnitur
#       -> drawers right
#       -> drawers left
#   -> Texture Set List
#       -> furnitur (material)
#       -> drawers (material)

import bpy

from bpy.props import *


# ----------------------------------------------------------------------------
# Class for all settings
# ----------------------------------------------------------------------------
class SubstanceProjectVariable(bpy.types.PropertyGroup):
    project_name = StringProperty()


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
    # Nominate project variable.
    del bpy.types.Scene.project_name
    del bpy.types.Scene.sppfile
    # Nominate texture set variable
    del bpy.types.Scene.tx_set_list
