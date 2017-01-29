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
        act_obj = context.active_object

        for mat in obj.material_slots:
            shader = bpy.data.materials
            row = layout.row(align=True)

            icon = "MATERIAL"
            row.prop(shader[mat.name], "name", text="", icon=icon)
            icon = "GROUP_UVS"
            row.operator("sbs_painter.uv_set", text="", icon=icon)

            liste = act_obj.material_slots
            index = liste.find(mat.name)

            if index > 0:
                icon = "SPACE3"
                ops = "sbs_painter.uv_set_on"
                row.operator(ops, text="", icon=icon).index = index

        name = "Add a Set"
        layout.operator("sbs_painter.uv_set_add", name)


def register():
    bpy.utils.register_class(TextureSetListPanel)


def unregister():
    bpy.utils.unregister_class(TextureSetListPanel)
