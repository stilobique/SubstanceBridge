# -----------------------------------------------------------------------------
# Substance Controller
#
# This file contains many function, name project, add texture set list...
# All function are create in an operator.
# 
# -----------------------------------------------------------------------------

import bpy

# ------------------------------------------------------------------------
# Function Name Project
# ------------------------------------------------------------------------
class CreateSubstanceProject(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "painter.substance_name"
    bl_label = "Create a new Substance Painter project"

    def execute(self, context):
        scn = context.scene
        slct_obj = bpy.context.selected_objects

        for obj in slct_obj:
            # Add attribute for all mesh selected
            obj['substance_project'] = scn.project_name

            # Add a materials basic.
            base_mat = bpy.data.materials.get(scn.project_name)
            if base_mat is None:
                base_mat = base_mat = bpy.data.materials.new(scn.project_name)

            # Asign materials to all object selected
            if obj.data.materials:
                obj.data.materials[0] = base_mat

            else:
                obj.data.materials.append(base_mat)

        return {'FINISHED'}


# ------------------------------------------------------------------------
# Function Selected Project
# ------------------------------------------------------------------------
class SelectedProject(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "painter.selected_project"
    bl_label = "Selected mesh with this project"

    def execute(self, context):
        scn = context.scene
        all_obj = bpy.data.objects

        for obj in all_obj:
            if obj.get('substance_project') is not None:
                name_obj = bpy.data.objects[obj.name]
                name_prj = bpy.data.objects[obj.name]['substance_project']

                if name_prj == scn.project_name:
                    # Selection object with a substance name.
                    name_obj.select = True

                else:
                    name_obj.select = False

        return {'FINISHED'}


# ------------------------------------------------------------------------
# Function unwrap set list
# ------------------------------------------------------------------------
class UVviewsSet(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "painter.uv_set"
    bl_label = "Unwrap mode for a texture set list"

    def execute(self, context):
        bpy.ops.painter.selected_project()
        bpy.ops.object.multi_object_uv_edit('INVOKE_DEFAULT')

        return {'FINISHED'}


def register():
    bpy.utils.register_class(CreateSubstanceProject)
    bpy.utils.register_class(SelectedProject)
    bpy.utils.register_class(UVviewsSet)


def unregister():
    bpy.utils.unregister_class(CreateSubstanceProject)
    bpy.utils.unregister_class(SelectedProject)
    bpy.utils.unregister_class(UVviewsSet)
