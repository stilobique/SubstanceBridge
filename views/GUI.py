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

        name = "New Project"
        layout.operator("object.painter_export", name).project = False

        layout.label("Substance Project")

        type_file = 'sppfile'
        layout.prop(context.scene, type_file)

        name = 'Update'
        layout.operator("object.painter_export", name).project = True


# -----------------------------------------------------------------------------
# Texture Set List panel
# -----------------------------------------------------------------------------
class TextureSetListPanel(bpy.types.Panel):
    bl_label = "Texture Set List"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Substances"

    def draw(self, context):
        layout = self.layout

        name = "Add a Set"
        layout.operator("object.painter_export", name).project = False


# -----------------------------------------------------------------------------
# Baking panel
# -----------------------------------------------------------------------------
class BakingSubstancePanel(bpy.types.Panel):
    bl_label = "Baking"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Substances"

    def draw(self, context):
        layout = self.layout

        name = "Baking map"
        layout.operator("object.painter_export", name).project = False
