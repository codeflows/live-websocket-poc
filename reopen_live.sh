echo "Quitting Live..."
osascript -e 'quit app "Live"'

sleep 1

echo "Restarting Live with sample project..."
open test_projects/Locators\ Project/Locators.als
