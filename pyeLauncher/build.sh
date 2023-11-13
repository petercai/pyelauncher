## create pyinstaller spec file
pyinstaller --clean --onedir --onefile --windowed \
                --icon=peppermint.jpg \
                -n peppermintLauncher \
                launcherApp.py



## build app file
pyinstaller --clean peppermintLauncher.spec



### dmgbuild: https://github.com/dmgbuild/dmgbuild
dmgbuild -s dmg/settings.py "PeppermintLauncher" PeppermintLauncher-macos-x86.dmg



### create-dmg: https://github.com/create-dmg/create-dmg
brew install create-dmg

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


open ~/Applications/SpringTools/SpringToolSuite4.app --args -data ~/workspace/sts/tmp

# Launcher gen
"~/Applications/SpringTools/SpringToolSuite4.app/Contents/MacOS/SpringToolSuite4" -data "~/workspace/sts/tmp" -name "Temp - SpringTools v4.29" -showlocation -clean -refresh  -vm "~/apps/homebrew/Cellar/openjdk/18.0.2.1/libexec/openjdk.jdk/Contents/Home/bin/java" -vmargs -Xms1024M -Xmx2048M
