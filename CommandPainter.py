import bpy
import tempfile
import subprocess

# Function to create an Obj, and export to painter
class ExportPainter(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.painter_export"
    bl_label = "Send mesh to painter export"
    
    def execute(self, context):
        # All variable for the script
        obj = bpy.context.active_object
        name = obj.name
        uv = bpy.data.meshes[name].uv_textures
        mesh = str('D:\\temps\\zob.obj')
        painterpath = str('D:\\Graflog\\Allegorithmic\\Substance Painter 2\\Substance Painter 2.exe')
        
        if obj.type == 'MESH':
            if uv:
                # Export du mesh selectionne
                bpy.ops.export_scene.obj(filepath=mesh, use_selection=True, path_mode='AUTO')
                
                # Call Substance Painter
                subprocess.call([painterpath, '--mesh', mesh])
            else:
                self.report({'WARNING'}, "This object don't containt a UV layers.")
                return {'CANCELLED'}

        else:
            self.report({'WARNING'}, "This object is not a mesh.")
            return {'CANCELLED'}

        return {'FINISHED'}