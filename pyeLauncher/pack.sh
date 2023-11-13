#!/bin/sh

test -f "PeppermintLauncher.dmg" && rm "PeppermintLauncher.dmg"
test -f "dist/PeppermintLauncher" && rm "dist/PeppermintLauncher"
create-dmg \
  --volname "PeppermintLauncher" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "PeppermintLauncher.app" 175 120 \
  --hide-extension "PeppermintLauncher.app" \
  --app-drop-link 425 120 \
  "PeppermintLauncher.dmg" \
  "dist/"

