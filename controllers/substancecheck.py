import bpy

import threading
import subprocess
import re

from ..models.SubstanceSoftware import *


class SubstanceCheck(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "substance.check"
    bl_label = "Check the number version and path to Substance Painter"

    path = bpy.props.StringProperty(
        name="Substance Painter Path",
    )

    def execute(self, context):
        SbsPainterVersion().start()

        return {'FINISHED'}


def register():
    bpy.utils.register_class(SubstanceCheck)


def unregister():
    bpy.utils.unregister_class(SubstanceCheck)
