import bpy

import bpy.utils.previews
import os

# icons_dict = bpy.utils.previews.new()
# icons_dir = os.path.join(os.path.dirname(__file__), "icons")
#
# script_path = r"../assets/icons/"
# icons_dir = os.path.join(os.path.dirname(script_path), "icons")
#
# icons_dict.load("custom_icon", os.path.join(icons_dir, "SPainter_logo.png"),
#                 'IMAGE')

# -----------------------------------------------------------------------------
# Show many options
# -----------------------------------------------------------------------------
class MoreOptPanel(bpy.types.Panel):
    bl_label = "Options"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Substances"

    def draw(self, context):
        layout = self.layout

        icon = 'PREFERENCES'
        name = "Show Settings"
        # layout.operator("sbs.settings", name, icon=icon)

        # icon = icons_dict["custom_icon"].icon_id
        # layout.operator("sbs.settings", name, icon=icon)


def register():
    global icons_dict
    bpy.utils.register_class(MoreOptPanel)

    icons_dict = bpy.utils.previews.new()
    script_path = r"../assets/icons/"
    icons_dir = os.path.join(os.path.dirname(script_path), "icons")

    icons_dict.load("custom_icon",
                    os.path.join(icons_dir, "SPainter_logo.png"),
                    'IMAGE')

    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_class(MoreOptPanel)

    bpy.utils.previews.remove(icons_dict)
    bpy.utils.unregister_module(__name__)