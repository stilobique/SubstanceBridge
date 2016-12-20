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


# class ProjectItem(bpy.types.PropertyGroup):
#     project_name = bpy.props.StringProperty(
#         name="Project Name",
#         description="Substance Project Name",
#         default="zozor",
#         )
#     # mesh = bpy.props.StringProperty(
#     #     name="Mesh",
#     #     description="Mesh used with this project",
#     #     )
#     # material = bpy.props.StringProperty(
#     #     name="Material",
#     #     description="Material used as Texture Set List",
#     #     )

#     # scn = bpy.context.scene
#     # scn['project_name'] = "Painter Project"

def initSceneSubstance(scn):
    bpy.types.Scene.project_name = StringProperty(
        name="Project")
    scn['project_name'] = "Painter Project"

    return


def register():
    # Déclaration variable scene.
    bpy.types.Scene.project_name = bpy.props.StringProperty(default="default")


def unregister():
    # Suppression des variables unasable.
    del bpy.types.Scene.project_name
