import bpy

# ------------------------------------------------------------------------
# Substance panel.
# ------------------------------------------------------------------------
class PainterPanel(bpy.types.Panel): 
    bl_label = "Painter Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Tools"
 
    def draw(self, context):
        self.layout.label(text="Substance Painter")
        self.layout.operator("object.painter_export", text="New Project")
        self.layout.operator("object.painter_export", text="Re-export")