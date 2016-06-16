import bpy
from bpy.props import StringProperty

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
        self.layout.operator("object.painter_export", text="New Project").project = False
        
        self.layout.label(text="Substance Painter Project")
        project_file = self.layout.prop(context.scene, 'sppfile')
        self.layout.operator("object.painter_export", text="Re-export").project = True