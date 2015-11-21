#!/bin/bash

set -e

ABLETON_VERSION=$1

if [ "$ABLETON_VERSION" = "beta" ]
then
  APP="Ableton Live 9.5 Beta"
  LOG_PATH="Live 9.5.1b2"
else
  APP="Ableton Live 9 Suite"
  LOG_PATH="Live 9.5"
fi

echo "Running LivePlaylist with $APP"

echo "Quitting Live..."
osascript -e "quit app \"$APP\""

sleep 1

echo "Installing LivePlaylist to Ableton remote scripts folder..."
TARGET="/Applications/$APP.app/Contents/App-Resources/MIDI Remote Scripts/LivePlaylist"
mkdir -p "$TARGET"
rm "$TARGET"/*.py* || true
cp src/*.py "$TARGET"

echo "Restarting Live with sample project..."
open -a "/Applications/$APP.app" "test_projects/Locators Project/Locators.als"

LOG_FILE="$HOME/Library/Preferences/Ableton/$LOG_PATH/Log.txt"
read -p "Press enter to tail Ableton log file at $LOG_FILE ..."
tail -f "$LOG_FILE"
