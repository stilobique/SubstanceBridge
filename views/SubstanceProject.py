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

        name = "New Project"
        layout.operator("object.painter_export", name).project = False

        layout.label("Substance Project")

        type_file = 'sppfile'
        layout.prop(context.scene, type_file)

        name = 'Update'
        layout.operator("object.painter_export", name).project = True

        # --------------------------------------------------------------------
        # Substance Project panel
        # --------------------------------------------------------------------

        layout.label("Debug Test")

        row = layout.row(align=True)
        icon = "GROUP"
        row.prop(scn, 'project_name', text='Painter Project', icon=icon)
        icon = "ZOOMIN"
        row.operator("painter.substance_name", text="", icon=icon)
        icon = "RESTRICT_SELECT_OFF"
        row.operator("painter.selected_project", text="", icon=icon)

        all_obj = bpy.data.objects

        for obj in all_obj:
            if obj.get('substance_project') is not None:
                name_obj = bpy.data.objects[obj.name]
                name_prj = bpy.data.objects[obj.name]['substance_project']
                layout.label(name_prj)



def register():
    bpy.utils.register_class(SubstanceProjectPanel)


def unregister():
    bpy.utils.unregister_class(SubstanceProjectPanel)
