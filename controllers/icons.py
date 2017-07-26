import bpy.utils.previews
import os

icons_dict = bpy.utils.previews.new()
icons_dir = os.path.join(os.path.dirname(__file__), "icons")

script_path = r"../assets/icons/"
icons_dir = os.path.join(os.path.dirname(script_path), "icons")

icons_dict.load("custom_icon", os.path.join(icons_dir, "SPainter_logo.png"),
                'IMAGE')

icon_value = icons_dict["custom_icon"].icon_id


# def register():
#     bpy.utils.register_class()
#
#
# def unregister():
#     bpy.utils.unregister_class()