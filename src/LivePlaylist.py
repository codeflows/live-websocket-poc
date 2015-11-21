from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer
import threading

class SimpleEcho(WebSocket):
   def handleMessage(self):
      self.sendMessage(self.data)

   def handleConnected(self):
      pass

   def handleClose(self):
      pass

import time

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

            self.server = SimpleWebSocketServer("", 55455, SimpleEcho)
            self.log_message('Started WS server')

            thread = threading.Thread(target=self.thread_run, args=())
            thread.daemon = True
            thread.start()
            self.log_message('Started background thread')

    def thread_run(self):
        self.log_message('THRIID!')

        """ Method that runs forever """
        while True:
            myFile = open('/Users/jaarnial/Projects/LivePlaylist/LivePlaylist/DEADBEEF.txt', 'w')
            myFile.write('remix.net test 1 2 3\n')
            myFile.close

            self.log_message('Doing something imporant in the background')

            time.sleep(2)

    def __cue_points_changed(self):
        for cp in self.song().cue_points:
            self.log_message('Cue points? %s %s' % (cp.name, cp.time))

    def update_display(self):
        self.log_message('Update display!')

        time1 = time.time()
        self.server.serve_one()
        time2 = time.time()
        self.log_message('One loop took %0.3f ms' % ((time2-time1)*1000.0))

        ControlSurface.update_display(self)
