# Project Substance
#  -> Name
#  -> Mesh
#     -> furnitur
#         -> materials (texture set list)
#     -> drawers right
#         -> materials (texture set list)
#     -> drawers left
#         -> materials (texture set list)

import bpy


def register():
    # Déclaration variable scene.
    bpy.types.Scene.project_name = \
        bpy.props.StringProperty(default="substance project")
    bpy.types.Scene.mesh_substance = \
        bpy.props.StringProperty(default="default")


def unregister():
    # Suppression des variables unasable.
    del bpy.types.Scene.project_name
    del bpy.types.Scene.mesh_substance
