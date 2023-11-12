pyinstaller --clean --onedir --onefile --windowed \
                --icon=peppermint.jpg \
                -n peppermintLauncher \
                launcherApp.py




pyinstaller --clean peppermintLauncher.spec



open ~/Applications/SpringToolSuite4.app --args -data $WS/sts/workspace
open ~/Applications/SpringTools/SpringToolSuite4.app --args -data ~/workspace/sts/tmp
open ~/Applications/SpringTools/SpringToolSuite4.app --args -data ~/workspace/sts/tmp

~/Applications/SpringTools/SpringToolSuite4.app -data ~/workspace/sts/tmp
~/Applications/SpringTools/SpringToolSuite4.app/Contents/MacOS/SpringToolSuite4 -data ~/workspace/sts/tmp

# Launcher gen
"~/Applications/SpringTools/SpringToolSuite4.app/Contents/MacOS/SpringToolSuite4" -data "~/workspace/sts/tmp" -name "Temp - SpringTools v4.29" -showlocation -clean -refresh  -vm "~/apps/homebrew/Cellar/openjdk/18.0.2.1/libexec/openjdk.jdk/Contents/Home/bin/java" -vmargs -Xms1024M -Xmx2048M

"~/Applications/SpringTools/SpringToolSuite4.app/Contents/MacOS/SpringToolSuite4" -data "~/workspace/sts/tmp" -name "Temp - SpringTools v4.29" -showlocation -clean -refresh  -vm "~/apps/homebrew/Cellar/openjdk/18.0.2.1/libexec/openjdk.jdk/Contents/Home/bin/java" -vmargs -Xms1024M -Xmx2048M 