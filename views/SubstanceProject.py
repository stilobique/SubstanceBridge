import bpy

from SubstanceBridge.models.project import ProjectItem


# -----------------------------------------------------------------------------
# Substance Project panel
# -----------------------------------------------------------------------------
class SubstanceProjectPanel(bpy.types.Panel):
    bl_label = "Substance Project"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Substances"

    def draw(self, context):
        layout = self.layout
        scn = context.scene

        name = "New Project"
        layout.operator("object.painter_export", name).project = False

        layout.label("Substance Project")

        type_file = 'sppfile'
        layout.prop(context.scene, type_file)

        name = 'Update'
        layout.operator("object.painter_export", name).project = True

        scn = context.scene

        row = layout.row(align=True)
        row.prop(scn, 'itemp_project', text='', icon="GROUP")
        # layout.operator("object.painter_group", "Last version")


def register():
    bpy.utils.register_class(SubstanceProjectPanel)


def unregister():
    bpy.utils.unregister_class(SubstanceProjectPanel)
