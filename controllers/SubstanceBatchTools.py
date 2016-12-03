import bpy


class BatchTools(bpy.types.Operator):
    sbs_baker = "sbs_baker"
    sbs_cooker = "sbs_cooker"
    sbs_mutator = "sbs_mutator"
    sbs_render = "sbs_render"


# ------------------------------------------
# Test pour récupérer tout les objects "high"
# ------------------------------------------


obj = bpy.data.objects
prefix_high = "_high"

enum_items = (
    ('FOO', 'foo', '',),
    ('BAR', 'bar', '')
)


class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Substances"

    def draw(self, context):
        layout = self.layout

        # obj = context.object

        col = layout.column()
        col.prop_search(context.scene, "coll_string", context.scene, "coll",
                        icon='OBJECT_DATA')


def populate_coll(scene):
    bpy.app.handlers.scene_update_pre.remove(populate_coll)
    scene.coll.clear()

    def mod_tuples(enum_items):
        for object in obj:
            # high in object.name
            if prefix_high in object.name:
                enum_items.insert(object.name)
        return enum_items
    for identifier, name, description in enum_items:
        scene.coll.add().name = name


def register():
    bpy.utils.register_module(__name__)

    bpy.types.Scene.coll = bpy.props.CollectionProperty(
        type=bpy.types.PropertyGroup
    )

    bpy.types.Scene.coll_string = bpy.props.StringProperty()

    # Hack for testing
    bpy.app.handlers.scene_update_pre.append(populate_coll)


def unregister():
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.coll
    del bpy.types.Scene.coll_string


if __name__ == "__main__":
    register()
