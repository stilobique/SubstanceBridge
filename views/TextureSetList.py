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
        all_obj = bpy.data.objects
        all_mat = bpy.data.materials
        nbr_item = len(all_mat)

        for mat in all_mat:
            name = "Materials : " + mat.name
            if obj.get('substance_project') is not None:
                i = 0
                while i < nbr_item:
                    layout.label(str(nbr_item))
                    i = i + 1

        layout.label("Old")

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
