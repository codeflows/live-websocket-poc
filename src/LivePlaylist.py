from __future__ import with_statement

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

import json

import Live
from _Framework.ControlSurface import ControlSurface

from Logger import Log
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer

# Annoying: json.dumps may return either str or unicode depending on input
# (e.g. for empty list, it returns str) and SimpleWebSocketServer expects unicode
# when sending string responses. Therefore wrapping everything in a non-empty
# unicode response here.
def to_json(data):
    wrapped = { u'response': data }
    return json.dumps(wrapped, encoding='utf-8', ensure_ascii=False)

queue = []

class SimpleEcho(WebSocket):
    def handleMessage(self):
        queue.append((self, self.data))

    def handleConnected(self):
        pass

    def handleClose(self):
        pass

class LivePlaylist(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            self.__c_instance = c_instance
            Log.set_logger(self.log_message)
            Log.log('LivePlaylist starting up')
            self.server = SimpleWebSocketServer("", 55455, SimpleEcho)

    def disconnect(self):
        Log.log('LivePlaylist shutting down')
        self.server.close()
        ControlSurface.disconnect(self)

    def update_display(self):
        self.server.serve_one()

        while len(queue) > 0:
            item = queue.pop(0)
            socket = item[0]
            command = item[1]
            Log.log("Execute %s" % command)
            if command == "list_cue_points":
                names = map(lambda cue: { u'name': cue.name }, self.get_song().cue_points)
                socket.sendMessage(to_json(names))
            else:
                Log.log("Unknown command!")

        ControlSurface.update_display(self)

    def get_song(self):
        return Live.Application.get_application().get_document()
