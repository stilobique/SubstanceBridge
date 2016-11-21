import bpy
from bpy.props import StringProperty

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
        self.layout.operator("object.painter_export", text="New Project").project = False
        project_file = self.layout.prop(context.scene, 'sppfile')
        self.layout.operator("object.painter_export", text="Re-export").project = True
        

        
# # ------------------------------------------------------------------------
# # Substance BatchTools panel.
# # ------------------------------------------------------------------------
# class BatchToolsPanel(bpy.types.Panel): 
    # bl_label = "Substance BatchTools"
    # bl_space_type = "VIEW_3D"
    # bl_region_type = "TOOLS"
    # bl_category = "Substances"
    
    # def draw(self, context):
        # layout = self.layout
        
        # layout.label(text="Baking")
        # # layout.prop_search(context.scene, "lp_name", context.scene, "lp_object", icon='OBJECT_DATA')
        
        # layout.prop_search(data, property, search_data, search_property, text, text_ctxt, translate, icon='OBJECT_DATA')

        # ob = context.object

        # split = layout.split()

        # col = split.column()
        # col.prop(ob, "parent", text="")
 