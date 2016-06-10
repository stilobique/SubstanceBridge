import bpy
import threading
import subprocess
import os

from SubstanceBridge.settings import SubstanceSettings

# ------------------------------------------------------------------------
# Create a class for a generic thread, else blender are block.
# ------------------------------------------------------------------------
class PainterThread(threading.Thread):
    def __init__(self):
        self.stdout = None
        self.stderr = None
        threading.Thread.__init__(self)

    def run(self):        
        temp_folder = bpy.app.tempdir
        temp_mesh = 'zob.obj'
        mesh = temp_folder + temp_mesh
        project = 'E:\\Documents\\Substance Painter\\samples\\Hans.spp'
        
        user_preferences = bpy.context.user_preferences
        addon_prefs = user_preferences.addons["SubstanceBridge"].preferences
        painter = str(addon_prefs.painterpath) # Set path for instant meshes
        
        popen = subprocess.call([painter, '--mesh', mesh])

# ------------------------------------------------------------------------
# Function to create an Obj, and export to painter
# ------------------------------------------------------------------------
class NewPainterProject(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.painter_export"
    bl_label = "Send mesh to painter export"
    
    def execute(self, context):
        # All variable for the script
        obj = bpy.context.active_object
     
        temp_folder = bpy.app.tempdir
        temp_mesh = 'zob.obj'
        mesh = temp_folder + temp_mesh
        
        # Test pour un nouveau project ou l'update d'un project.
        if project:
            print("Update project mother fucker.")
        
        else:
            print("New Project Painter.")
            # if obj.type == 'MESH':
                # if bpy.data.meshes[obj.name].uv_textures:
                    # # Export du mesh selectionne
                    # bpy.ops.export_scene.obj(filepath=mesh, use_selection=True, path_mode='AUTO')

                    # user_preferences = bpy.context.user_preferences
                    # addon_prefs = user_preferences.addons["SubstanceBridge"].preferences
                    # painter = str(addon_prefs.painterpath) # Set path for instant meshes
                    
                    # # Verification si le soft est configuré dans le path
                    # if painter:
                        # """Launch substance painter program."""
                        # myclass = PainterThread()
                        # myclass.start()

                    # else:
                        # self.report({'WARNING'}, "No path configured, setup into User Pre.")
                        # return {'CANCELLED'}

                # else:
                    # self.report({'WARNING'}, "This object don't containt a UV layers.")
                    # return {'CANCELLED'}

            # else:
                # self.report({'WARNING'}, "This object is not a mesh.")
                # return {'CANCELLED'}

        return {'FINISHED'}