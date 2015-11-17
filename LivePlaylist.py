from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface

class LivePlaylist(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            self.__c_instance = c_instance
            self.show_message('test')
