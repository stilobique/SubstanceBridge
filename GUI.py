import bpy
from bpy.props import StringProperty, BoolProperty

# ------------------------------------------------------------------------
# Substance panel.
# ------------------------------------------------------------------------
class PainterPanel(bpy.types.Panel): 
    bl_label = "Painter Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Tools"

    bpy.types.Scene.sppfile = StringProperty \
        (
        name = ".spp file",
        description = "Field project path",
        subtype = 'FILE_PATH'
        )
 
    def draw(self, context):
        self.layout.label(text="Substance Painter")
        self.layout.operator("object.painter_export", text="New Project").project = False
        
        self.layout.label(text="Substance Painter Project")
        self.layout.prop(context.scene, 'sppfile')
        self.layout.operator("object.painter_export", text="Re-export").project = True