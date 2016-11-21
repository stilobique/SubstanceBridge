import bpy

# from SubstanceBridge import list_high

# ------------------------------------------------------------------------
# Substance Painter panel.
# ------------------------------------------------------------------------
class PainterPanel(bpy.types.Panel):
    bl_label = "Substance Painter"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Substances"

    def draw(self, context):
        layout = self.layout

        name = "New Project"
        layout.operator("object.painter_export", name).project = False

        type_file = 'sppfile'
        layout.prop(context.scene, type_file)

        name = 'Update'
        layout.operator("object.painter_export", name).project = True

        name = 'Texturing List'
        layout.operator("group.create", name)
