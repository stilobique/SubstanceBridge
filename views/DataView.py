import bpy


# -----------------------------------------------------------------------------
# Substance Project panel
# -----------------------------------------------------------------------------
class SubstanceData(bpy.types.Panel):
    bl_label = "Substance Project"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "data"

    def draw(self, context):
        layout = self.layout

        layout.label("Project Name")


def register():
    bpy.utils.register_class(SubstanceData)


def unregister():
    bpy.utils.unregister_class(SubstanceData)
