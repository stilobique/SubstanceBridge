import bpy
import threading
import subprocess
import os

from bpy.props import StringProperty, BoolProperty
from SubstanceBridge.settings import SubstanceSettings

# ------------------------------------------------------------------------
# Create a class for a generic thread, else blender are block.
# ------------------------------------------------------------------------
class SubstancePainterThread(threading.Thread):
    def __init__(self, path_painter, path_project):
        threading.Thread.__init__(self)
        self.path_painter = path_painter
        self.path_project = path_project
        
    def run(self):
        temp_folder = bpy.app.tempdir
        temp_mesh = 'tmp.obj'
        mesh = temp_folder + temp_mesh
        if self.path_project == "":
            popen = subprocess.call([self.path_painter, '--mesh', mesh])
            
        else:
            popen = subprocess.call([self.path_painter, '--mesh', mesh, self.path_project])

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
        
    update = BoolProperty(
        default = False,
        name = "Variable de test, update or not"
        )
        
    path_project = StringProperty(
        name = "Path Substance project"
        )

    def execute(self, context):
        # All variable for the script
        obj = bpy.context.active_object
     
        temp_folder = bpy.app.tempdir
        temp_mesh = 'tmp.obj'
        mesh = temp_folder + temp_mesh
        
        user_preferences = bpy.context.user_preferences
        addon_prefs = user_preferences.addons["SubstanceBridge"].preferences
        self.painter = str(addon_prefs.painterpath) # Set path for instant meshes
        
        if obj.type == 'MESH':
            if bpy.data.meshes[obj.name].uv_textures:
                # Export du mesh selectionne
                bpy.ops.export_scene.obj(filepath=mesh, use_selection=True, path_mode='AUTO')
                
                # Verification si le soft est configuré dans le path
                if self.painter:
                    # Test If it's a new project.
                    if self.project == True:
                        path_sppfile = os.path.abspath(bpy.context.scene.sppfile)
                        self.path_project = path_sppfile
                        launchpainter = SubstancePainterThread(self.painter, self.path_project)
                        launchpainter.start()
                    else:
                        self.path_project = ""
                        launchpainter = SubstancePainterThread(self.painter, self.path_project)
                        launchpainter.start()
                else:
                    self.report({'WARNING'}, "No path configured, setup into User Pre.")
                    return {'CANCELLED'}

            else:
                self.report({'WARNING'}, "This object don't containt a UV layers.")
                return {'CANCELLED'}

        else:
            self.report({'WARNING'}, "This object is not a mesh.")
            return {'CANCELLED'}

        return {'FINISHED'}