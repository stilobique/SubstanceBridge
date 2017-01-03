import bpy


# -----------------------------------------------------------------------------
# Function Debug, show many proporties
# -----------------------------------------------------------------------------
class DebugShow(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "debug.sbs_data"
    bl_label = "A function to show many substance data debug"

    def execute(self, context):
        scn = context.scene

        # Substance Variable
        sbs_name = scn.sbs_project_settings.prj_name
        sbs_path_spp = scn.sbs_project_settings.path_spp

        print("Substance Project : ", sbs_name)
        print("Link spp file : ", sbs_path_spp)

        return {'FINISHED'}


# -----------------------------------------------------------------------------
# Substance Project panel
# -----------------------------------------------------------------------------
class DebugPanel(bpy.types.Panel):
    bl_label = "Debug"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Substances"

    def draw(self, context):
        layout = self.layout
        scn = context.scene

        layout.label("Debug Call")

        layout.operator("debug.sbs_data", text="Debug Sbs")


def register():
    bpy.utils.register_class(DebugShow)
    bpy.utils.register_class(DebugPanel)


def unregister():
    bpy.utils.unregister_class(DebugShow)
    bpy.utils.unregister_class(DebugPanel)
