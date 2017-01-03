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
        obj = context.object

        layout.label("Project Name")
        row = layout.row(align=True)
        data = scn.sbs_project_settings
        row.prop(data, 'prj_name', text="")
        icon = "ZOOMIN"
        row.operator("painter.substance_name", text="", icon=icon)
        icon = "RESTRICT_SELECT_OFF"
        row.operator("painter.selected_project", text="", icon=icon)

        if obj.get("substance_project") is None:
            # Not Substance Project in this blend-file
            layout.label("Create a New Project")

        else:
            name = "Export New Project"
            ops = "object.painter_export"
            layout.operator(ops, name).project = False

            data = scn.sbs_project_settings
            layout.prop(data, 'path_spp', text="")

            name = 'Export Update'
            icon = 'FILE_REFRESH'
            layout.operator(ops, name, icon=icon).project = True


def register():
    bpy.utils.register_class(SubstanceProjectPanel)


def unregister():
    bpy.utils.unregister_class(SubstanceProjectPanel)
