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


class ProjectItem(bpy.types.PropertyGroup):
    project_name = bpy.props.StringProperty(
        name="Project Name",
        description="Substance Project Name",
        default="zozor",
        )
    # mesh = bpy.props.StringProperty(
    #     name="Mesh",
    #     description="Mesh used with this project",
    #     )
    # material = bpy.props.StringProperty(
    #     name="Material",
    #     description="Material used as Texture Set List",
    #     )

    scn = bpy.context.scene
    scn['project_name'] = "Painter Project"


def register():
    bpy.utils.register_class(ProjectItem)

    bpy.types.Scene.item_project = \
        bpy.props.CollectionProperty(type=ProjectItem)


def unregister():
    bpy.utils.unregister_class(ProjectItem)
