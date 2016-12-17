import bpy


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
        # name_prj = SubstanceBridge.initVariable.ProjectName

        name = "New Project"
        layout.operator("object.painter_export", name).project = False

        layout.label("Substance Project")

        type_file = 'sppfile'
        layout.prop(context.scene, type_file)

        name = 'Update'
        layout.operator("object.painter_export", name).project = True


def register():
    bpy.utils.register_class(SubstanceProjectPanel)


def unregister():
    bpy.utils.unregister_class(SubstanceProjectPanel)
