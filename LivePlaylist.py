from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface

class LivePlaylist(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            self.__c_instance = c_instance
            self.log_message('LivePlaylist starting up')
            self.song().add_is_playing_listener(self.__playing_status_changed)

    def __playing_status_changed(self):
        self.log_message('Playing? %s' % self.song().is_playing)
