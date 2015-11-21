echo "Syncing LivePlaylist to Ableton remote scripts folder..."
TARGET=/Applications/Ableton\ Live\ 9.5\ Beta.app/Contents/App-Resources/MIDI\ Remote\ Scripts/LivePlaylist
rm "$TARGET"/*.py* || true
cp src/*.py "$TARGET"
