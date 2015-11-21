echo "Quitting Live..."
osascript -e 'quit app "Ableton Live 9.5 Beta"'

sleep 1

echo "Restarting Live with sample project..."
open test_projects/Locators\ Project/Locators.als
