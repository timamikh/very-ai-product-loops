@echo off
rem Double-click to open the console. Windows.
rem
rem The console's audience is the product manager, and a terminal is a wall for that reader, so the
rem command they were told to type lives in a file they can open instead. It does exactly what the
rem README documents, in the folder it sits in, with no arguments to remember.
rem
rem ASCII only, on purpose: a console window on Windows may not be reading UTF-8, and a dash that
rem arrives as a box is the same failure this project refuses everywhere else.
rem
rem macOS and Linux: use console.command next to this file.

setlocal
cd /d "%~dp0..\.."

set "PY="
where py >nul 2>nul && set "PY=py -3"
if not defined PY where python >nul 2>nul && set "PY=python"

if not defined PY (
  echo.
  echo   Python 3 is missing. It is all this needs, and it is the only thing missing.
  echo   Install it from https://www.python.org/downloads/ ^(tick "Add python.exe to PATH"^)
  echo   and double-click this file again.
  echo.
  pause
  exit /b 1
)

echo.
echo   Opening the console in your browser. It only reads the product folder, it changes nothing.
echo   Close this window, or press Ctrl+C, to stop it.
echo.

%PY% tools\ui\serve.py %*
pause
