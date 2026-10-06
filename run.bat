@echo off
setlocal
cd /d "%~dp0"
call "%~dp0start.bat" --setup-only
if errorlevel 1 exit /b 1
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0run.ps1"
if errorlevel 1 pause
