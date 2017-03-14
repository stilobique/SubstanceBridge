import bpy

import threading
import subprocess


class SubstanceCheckThread(threading.Thread):

    def __init__(self, path_painter):
        threading.Thread.__init__(self)
        self.path_painter = path_painter

    def run(self):
        subprocess.call([self.path_painter, '-v'])


def register():
    bpy.utils.register_class(SubstanceCheckThread)


def unregister():
    bpy.utils.unregister_class(SubstanceCheckThread)
