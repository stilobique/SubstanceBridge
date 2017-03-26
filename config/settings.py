import bpy

from .. import addon_updater_ops

# Import all variable setup
from ..models.paths import SbsModelsSetup
from ..models.addon_updater_setup import UpdaterVariables


# -----------------------------------------------------------------------------
# Settings for this addons
# -----------------------------------------------------------------------------
class SubstanceSettings(bpy.types.AddonPreferences):
    bl_idname = "SubstanceBridge"

    # addon updater preferences from `__init__`, be sure to copy all of them
    auto_check_update = UpdaterVariables.auto_check_update

    updater_intrval_months = UpdaterVariables.updater_intrval_months
    updater_intrval_days = UpdaterVariables.updater_intrval_days
    updater_intrval_hours = UpdaterVariables.updater_intrval_hours
    updater_intrval_minutes = UpdaterVariables.updater_intrval_minutes

    # All software path.
    path_painter = SbsModelsSetup.path_painter

    def draw(self, context):
        layout = self.layout
        layout.label(text="Substance Path.")

        row = layout.row(align=False)
        row.prop(self, "path_painter")
        row.operator("substance.check", text="Check").path = self.path_painter
        # layout.prop(self, "path_batchtools")
        # layout.prop(self, "path_designer")

        # Show UI updater Addon
        addon_updater_ops.update_settings_ui(self, context)


def register():
    bpy.utils.register_class(SubstanceSettings)


def unregister():
    bpy.utils.unregister_class(SubstanceSettings)
