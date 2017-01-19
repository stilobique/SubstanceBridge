# -----------------------------------------------------------------------------
# Substance Painter
#
# This file contains controlle all Substance Painter functions, send to SP, or
# re-export an project.
# -----------------------------------------------------------------------------

import bpy
import threading
import subprocess
import SubstanceBridge

from bpy.props import StringProperty, BoolProperty

# ------------------------------------------------------------------------
# Create a class for a generic thread, else blender are block.
# ------------------------------------------------------------------------


class SubstancePainterThread(threading.Thread):

    def __init__(self, path_painter, path_project):
        threading.Thread.__init__(self)
        self.path_painter = path_painter
        self.path_project = path_project

    def run(self):
        mesh = SubstanceBridge.models.project.SubstanceVariable.tmp_mesh
        if self.path_project == "":
            popen = subprocess.call([self.path_painter, '--mesh', mesh])

        else:
            popen = subprocess.call([self.path_painter,
                                     '--mesh',
                                     mesh,
                                     self.path_project])

# ------------------------------------------------------------------------
# Function to create an Obj, and export to painter
# ------------------------------------------------------------------------


class SendToPainter(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.painter_export"
    bl_label = "Send mesh to painter export"

    project = BoolProperty(name="It's a new project.")
    painter = StringProperty(name="Path Substance Painter")
    update = BoolProperty(
        default=False,
        name="Variable de test, update or not"
        )

    path_project = StringProperty(name="Path Substance project")

    def execute(self, context):
        obj = bpy.context.active_object
        mesh = SubstanceBridge.models.project.SubstanceVariable.tmp_mesh

        user_preferences = bpy.context.user_preferences
        addon_prefs = user_preferences.addons["SubstanceBridge"].preferences
        self.painter = str(addon_prefs.painterpath)

        print("path mesh")
        print(mesh)
        print("----------")
        print("obj file name")
        print(SubstanceBridge.models.project.SubstanceVariable.mesh_name)

        if obj.type == 'MESH':
            obj_mesh = bpy.data.objects[obj.name].data
            if obj_mesh.uv_textures:
                # Export du mesh selectionne
                bpy.ops.painter.selected_project()
                bpy.ops.export_scene.obj(filepath=mesh,
                                         use_selection=True,
                                         use_materials=True,
                                         path_mode='AUTO')

                # Verification si le soft est configuré dans le path
                if self.painter:
                    scn = context.scene
                    path_sppfile = scn.sbs_project_settings.path_spp
                    # Test If it's a new project.
                    if self.project is True:
                        self.path_project = path_sppfile

                    else:
                        self.path_project = ""

                    launchpainter = SubstancePainterThread(self.painter,
                                                           self.path_project)
                    launchpainter.start()
                else:
                    self.report({'WARNING'},
                                "No path configured, setup into User Pre.")
                    return {'CANCELLED'}

            else:
                self.report({'WARNING'},
                            "This object don't containt a UV layers.")
                return {'CANCELLED'}

        else:
            self.report({'WARNING'}, "This object is not a mesh.")
            return {'CANCELLED'}

        return {'FINISHED'}


def register():
    bpy.utils.register_class(SendToPainter)


def unregister():
    bpy.utils.unregister_class(SendToPainter)
