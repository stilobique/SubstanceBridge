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

        # Materials from selected Obj.
        layout.prop(obj, "active_material", text="")

        icon = "GROUP"
        row.prop(scn, 'project_name', text="", icon=icon)

        name = "Add a Set"
        layout.operator("object.painter_export", name).project = False


def register():
    bpy.utils.register_class(TextureSetListPanel)


def unregister():
    bpy.utils.unregister_class(TextureSetListPanel)
