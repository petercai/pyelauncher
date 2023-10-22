pyinstaller --clean --onedir --onefile --windowed \
                --icon=peppermint.jpg \
                -n peppermintLauncher \
                launcherApp.py




pyinstaller --clean peppermintLauncher.spec
