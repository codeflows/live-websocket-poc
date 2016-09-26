[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

Quick proof-of-concept of running a single-threaded WebSocket server (based on [SimpleWebSocketServer](https://github.com/dpallot/simple-websocket-server/)) inside a Ableton Live MIDI script.

The WebSocket interface accepts two types of messages: one for listing cue points and one for starting playback from a cue point. There's a crude HTML client in the [client subdirectory](client)

Works with Live 9.5.1 beta 2, which includes Python 2.7 support

## Disclaimer

This project has no affiliation with Ableton.

## Inspiration

- https://github.com/dpallot/simple-websocket-server
- https://github.com/Mystfit/Showtime-Live
- https://github.com/valsteen/ableton-live-webapi
