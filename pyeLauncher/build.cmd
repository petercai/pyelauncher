
@echo off

set PYE_HOME=%~dp0

if "%1" ==  "" goto :USAGE
if ""%1"" == ""spec"" goto spec
if ""%1"" == ""build"" goto build
if ""%1"" == ""clean"" goto clean

:spec
set OPTION=--clean --onedir --onefile --windowed ^
              --icon=peppermint.jpg ^
              -n peppermintLauncher 
              @REM --add-data="config/elauncher.xml:config" ^
@REM set OPTION=--clean --onefile --onedir --windowed --icon=peppermint.jpg -n pyelauncher 
pyinstaller %OPTION% launcherApp.py
goto END

:build
pyinstaller --clean peppermintLauncher.spec
goto END
:clean
deltree  dist build
goto END

:USAGE
@echo "build [spec|build|clean]"

:END