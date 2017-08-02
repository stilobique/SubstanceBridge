import threading
import subprocess
import bpy

"""
This models create all substance software class, you can easily use this 
class to call a software, this number version, this path or many option.
"""


class SbsPainter(threading.Thread):
    """This class is a shell for all inherited class

    https://docs.allegorithmic.com/documentation/display/SPDOC/Command+Lines
    """

    def __init__(self):
        threading.Thread.__init__(self)
        self.path_painter = bpy.context.user_preferences.addons[
            "SubstanceBridge"].preferences.path_painter


class SbsPainterProject(SbsPainter):
    """Substance Painter Thread, any argument to launch an new instance
    project, check the Painter Version and other action.

    You can find all Substance Painter Command Lines on Allegorithmic
    documentation.
    """
    def __init__(self, path_project, name_project):
        SbsPainter.__init__(self)
        self.path_project = path_project
        self.name_project = name_project

    def run(self):
        if self.path_project == "":
            subprocess.call([self.path_painter,'--mesh',self.name_project,])

        else:
            subprocess.call([self.path_painter,
                             '--mesh',
                             self.name_project,
                             self.path_project,
                             ])

class SbsPainterVersion(SbsPainter):
    """Substance Painter Version call Substance Painter"""
    def run(self):
        subprocess.call([self.path_painter, '-version',])
