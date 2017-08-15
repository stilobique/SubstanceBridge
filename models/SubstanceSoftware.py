import threading
import subprocess
import bpy

"""
This models create all substance software class, you can easily use this 
class to call a software, this number version, this path or many option.
"""


class SbsPainter(threading.Thread):
    """Principal Class, make a bridge between Substance Painter and Blender.

    Can be improve with many idea, check the process and why not restart it,
    check if the painter path has good...

    More Command Line painter available on Allegorithmic documentation :
    https://docs.allegorithmic.com/documentation/display/SPDOC/Command+Lines
    """

    def __init__(self):
        threading.Thread.__init__(self)
        self.path_painter = bpy.context.user_preferences.addons[
            "SubstanceBridge"].preferences.path_painter


class SbsPainterProject(SbsPainter):
    """Inherited class, export a mesh from Blender to Painter. Need two
    arguments :
    - The temporary folder
    - The Substance Project Name.
    """
    def __init__(self, path_project, name_project):
        SbsPainter.__init__(self)
        self.path_project = path_project
        self.name_project = name_project

    def run(self):
        if self.path_project == "":
            subprocess.call([self.path_painter, '--mesh', self.name_project])

        else:
            subprocess.call([self.path_painter,
                             '--mesh',
                             self.name_project,
                             self.path_project,
                             ])


class SbsPainterVersion(SbsPainter):
    """Inherited class ; call Painter with a request, the Substance Painter
    version number."""
    def run(self):
        subprocess.call([self.path_painter, '-version'])
