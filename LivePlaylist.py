from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface

class LivePlaylist(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            self.__c_instance = c_instance
            self.log_message('LivePlaylist starting up')
            self.song().add_cue_points_listener(self.__cue_points_changed)
            self.__cue_points_changed()
            import platform
            self.log_message(platform.python_version())

    def __cue_points_changed(self):
        for cp in self.song().cue_points:
            self.log_message('Cue points? %s %s' % (cp.name, cp.time))
