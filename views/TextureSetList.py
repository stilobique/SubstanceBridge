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
        scn = context.scene
        obj = context.object

        # Materials from selected Obj.
        row = layout.row(align=True)
        row.prop(obj, "active_material", text="")
        icon = "GROUP_UVS"
        row.operator_context = "INVOKE_DEFAULT"
        row.operator("painter.uv_set", text="", icon=icon)

        layout.operator("object.multi_object_uv_edit",
                             text="Multi Object UV Editing",
                             icon="IMAGE_RGB")

        row = layout.row(align=True)
        icon = "GROUP"
        row.prop(scn, 'project_name', text="", icon=icon)

        icon = "MATERIAL"
        row.operator("painter.selected_project", text="", icon=icon)

        name = "Add a Set"
        layout.operator("object.painter_export", name).project = False


def register():
    bpy.utils.register_class(TextureSetListPanel)


def unregister():
    bpy.utils.unregister_class(TextureSetListPanel)
