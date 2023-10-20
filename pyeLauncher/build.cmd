
@echo off

@REM pyi-makespec -F -D -w -X  name.py [other scripts …]
@REM pyinstaller --clean launcherApp.py

set PYE_HOME=%~dp0
set ECLIPSE_HOME=C:\dev\eclipse\eclipse-rcp-202209\eclipse.exe


if "%1" ==  "" goto :USAGE
if ""%1"" == ""spec"" goto spec
if ""%1"" == ""build"" goto build
if ""%1"" == ""clean"" goto clean

:spec
set OPTION=-F -D -w --icon=C:\dev\eclipse\eclipse-rcp-202209\eclipse.exe,0 -n pyelauncher 
@REM %PYTHON_HOME%\python.exe %PYINST_HOME%\building\Makespec.py %OPTION% launcherApp.py
pyinstaller %OPTION% launcherApp.py
goto END

:build
pyinstaller pyelauncher.spec
goto END
:clean
deltree  dist build
goto END

:USAGE
@echo "build [spec|build|clean]"

:END