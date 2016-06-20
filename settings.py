import bpy

from bpy.props import StringProperty, IntProperty, BoolProperty

# ------------------------------------------------------------------------
# Settings for this addons
# ------------------------------------------------------------------------
class SubstanceSettings(bpy.types.AddonPreferences):
    bl_idname = "SubstanceBridge"

    # All software path.
    painterpath = StringProperty(
            name = "Substance Painter",
            subtype = "FILE_PATH",
            )
    path_designer = StringProperty(
            name="Substance Designer",
            subtype='FILE_PATH',
            )
    path_batchtools = StringProperty(
            name="Batch Tools",
            subtype='DIR_PATH',
            )
            
    # Project Path.
    projectpath = StringProperty(
            name="path Spp files",
            subtype='FILE_PATH',
            )
            
    def draw(self, context):
        layout = self.layout
        layout.label(text="All substance path.")
        layout.prop(self, "painterpath")
        layout.prop(self, "path_batchtools")
        layout.prop(self, "path_designer")

	
def register():
    bpy.utils.register_class(SubstanceSettings)


def unregister():
    bpy.utils.unregister_class(SubstanceSettings)