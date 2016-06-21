import bpy

def list_high(scene):
    bpy.app.handlers.scene_update_pre.remove(list_high)
    scene.hp_object.clear()
    
    object = bpy.data.objects
    for obj in object:
        print(obj.name)

class BatchTools(bpy.types.Operator):
    sbs_baker = "sbs_baker"
    sbs_cooker = "sbs_cooker"
    sbs_mutator = "sbs_mutator"
    sbs_render = "sbs_render"