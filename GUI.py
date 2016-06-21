import bpy
from bpy.props import StringProperty

# ------------------------------------------------------------------------
# Substance Painter panel.
# ------------------------------------------------------------------------
class PainterPanel(bpy.types.Panel): 
    bl_label = "Substance Painter"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_category = "Substances"
    bl_category = "Tools"
            
    def draw(self, context):
        self.layout.label(text="Substance Painter")
        self.layout.operator("object.painter_export", text="New Project").project = False
        
        self.layout.label(text="Substance Painter Project")
        project_file = self.layout.prop(context.scene, 'sppfile')
        self.layout.operator("object.painter_export", text="Re-export").project = True
        
        
# ------------------------------------------------------------------------
# Substance BatchTools panel.
# ------------------------------------------------------------------------
class BatchToolsPanel(bpy.types.Panel): 
    bl_label = "Substance BatchTools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_category = "Substances"
    bl_category = "Tools"
            
    def draw(self, context):
        self.layout.label(text="Baking")
        self.layout.prop_search(context.scene, "hp_name", context.scene, "hp_object", icon='OBJECT_DATA')