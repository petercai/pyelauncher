@echo off

set PYE_HOME=%~dp0
set PYINST_HOME=F:\python\pyinstaller-1.4
set PYTHON_HOME=F:\Python25
set ECLIPSE_HOME=F:\java\eclipse\Helios\eclipse


if "%1" ==  "" goto :USAGE
if ""%1"" == ""config"" goto config
if ""%1"" == ""spec"" goto spec
if ""%1"" == ""build"" goto build
if ""%1"" == ""clean"" goto clean

:config
pushd %PYINST_HOME%
%PYTHON_HOME%\python.exe Configure.py
popod
goto END
:spec
set OPTION=-F -D -w -X --icon=F:\java\eclipse\Helios\eclipse\eclipse.exe,0 -n pyelauncher 
%PYTHON_HOME%\python.exe %PYINST_HOME%\Makespec.py %OPTION% launcherApp.py
goto END
:build
%PYTHON_HOME%\python.exe %PYINST_HOME%\Build.py pyelauncher.spec
goto END
:clean
deltree  dist build
goto END

:USAGE
@echo "build.bat [config|spec|build|clean]"

:END