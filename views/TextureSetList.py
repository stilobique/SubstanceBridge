import bpy


# -----------------------------------------------------------------------------
# Texture Set List panel
# -----------------------------------------------------------------------------
class TextureSetListPanel(bpy.types.Panel):
    bl_label = "Texture Set List"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Substances"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        layout.label("Texture Set List")
        row = layout.row(align=True)
        row.prop(obj, "active_material", text="")
        icon = "GROUP_UVS"
        row.operator("painter.uv_set", text="", icon=icon)

        name = "Add a Set"
        layout.operator("painter.uv_set_add", name)


def register():
    bpy.utils.register_class(TextureSetListPanel)


def unregister():
    bpy.utils.unregister_class(TextureSetListPanel)
