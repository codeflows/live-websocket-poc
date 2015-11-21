from __future__ import with_statement

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

import Live
from _Framework.ControlSurface import ControlSurface

from Logger import Log
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer

class SimpleEcho(WebSocket):
    def handleMessage(self):
        Log.log("Websocket echoing back %s" % self.data)
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
            Log.set_logger(self.log_message)
            Log.log('LivePlaylist starting up')
            self.server = SimpleWebSocketServer("", 55455, SimpleEcho)

    def update_display(self):
        Log.log('START')
        time1 = time.time()
        self.server.serve_one()
        time2 = time.time()
        Log.log('DONE in %0.3f ms' % ((time2-time1)*1000.0))

        ControlSurface.update_display(self)
