import bpy


# -----------------------------------------------------------------------------
# Substance Project panel
# -----------------------------------------------------------------------------
class SubstanceData(bpy.types.Panel):
    bl_label = "Substance Data"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        obj_slt = context.active_object

        return obj_slt is not None and obj_slt.type == 'MESH'

    def draw(self, context):
        layout = self.layout
        ob = context.object

        # Substance Info save in object and data mesh.
        if ob.get('substance_project') is not None:
            layout.label("Sbs Project Name : ")
            layout.label(ob['substance_project'])

        # Debug Option
        layout.label("Debug Call")
        layout.operator("debug.sbs_data", text="Debug Sbs")

        me = context.mesh
        layout.template_list("MESH_UL_uvmaps_vcols",
                             "uvmaps",
                             me,
                             "uv_textures",
                             me.uv_textures,
                             "active_index",
                             rows=1)

        # me = context.mesh
        # layout.template_list("MESH_UL_uvmaps_vcols",
        #                      "uvmaps",
        #                      me,
        #                      "uv_textures",
        #                      me.uv_textures,
        #                      "active_index",
        #                      rows=1)


def register():
    bpy.utils.register_class(SubstanceData)


def unregister():
    bpy.utils.unregister_class(SubstanceData)
