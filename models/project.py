# Project Substance
#  -> Name -> String
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
    mesh_list = []
    texture_set_list = []
    painterpath = StringProperty(
            name="Substance Painter",
            subtype="FILE_PATH",
            )


def register():
    # Déclaration variable scene.
    bpy.types.Scene.project_name = \
        bpy.props.StringProperty(default="substance project")
    bpy.types.Scene.texture_set_list = \
        bpy.props.StringProperty(default="default")


def unregister():
    # Suppression des variables unasable.
    del bpy.types.Scene.project_name
    del bpy.types.Scene.mesh_substance
