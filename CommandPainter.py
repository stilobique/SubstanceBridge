import bpy
import threading
import subprocess
import os

from bpy.props import StringProperty, BoolProperty
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
class PainterProject(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.painter_export"
    bl_label = "Send mesh to painter export"

    project = BoolProperty(
        name = "It's a new project."
        )
        
    painter = StringProperty(
        name = "Path Substance Painter"
        )

    path_project = StringProperty(
        name = "Path Project"
        )
        
    sppfile = StringProperty(
        name = "Path Project Painter"
        )
        
    def execute(self, context):
        # All variable for the script
        obj = bpy.context.active_object
     
        temp_folder = bpy.app.tempdir
        temp_mesh = 'zob.obj'
        mesh = temp_folder + temp_mesh
        
        # Test pour un nouveau project ou l'update d'un project.
        if self.project == True:
            user_preferences = bpy.context.user_preferences
            addon_prefs = user_preferences.addons["SubstanceBridge"].preferences
            self.painter = str(addon_prefs.painterpath) # Set path for instant meshes
                    
            print("path du spp file : ", self.path_project) # Debug lines
            print("path du spp file 2 : ", bpy.context.scene.sppfile) # Debug lines
            print("Project variable : ", self.project) # Debug lines
            print("painter : ", self.painter) # Debug lines
        
        # Il s'agit d'un nouveau project.
        else:
            if obj.type == 'MESH':
                if bpy.data.meshes[obj.name].uv_textures:
                    # Export du mesh selectionne
                    bpy.ops.export_scene.obj(filepath=mesh, use_selection=True, path_mode='AUTO')
                    user_preferences = bpy.context.user_preferences
                    addon_prefs = user_preferences.addons["SubstanceBridge"].preferences
                    self.painter = str(addon_prefs.painterpath) # Set path for instant meshes
                    # Verification si le soft est configuré dans le path
                    if self.painter:
                        """Launch substance painter program."""
                        myclass = PainterThread()
                        myclass.start()

                    else:
                        print("path de substance painter %s : ", self.painter) # Debug lines
                        self.report({'WARNING'}, "No path configured, setup into User Pre.")
                        return {'CANCELLED'}

                else:
                    self.report({'WARNING'}, "This object don't containt a UV layers.")
                    return {'CANCELLED'}

            else:
                self.report({'WARNING'}, "This object is not a mesh.")
                return {'CANCELLED'}

        return {'FINISHED'}