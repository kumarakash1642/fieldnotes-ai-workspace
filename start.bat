@echo off
setlocal
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" goto run
echo Creating the local Python environment...
where py >nul 2>nul
if not errorlevel 1 (
  py -3 -m venv .venv
) else (
  where python >nul 2>nul
  if not errorlevel 1 (
    python -m venv .venv
  ) else (
    if exist "%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" (
      "%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -m venv .venv
    ) else (
      echo Python 3.10 or newer is needed. Install Python and run this file again.
      pause
      exit /b 1
    )
  )
)
if not exist ".venv\Scripts\python.exe" (
  echo Could not create the Python environment.
  pause
  exit /b 1
)
:run
".venv\Scripts\python.exe" -c "import flask, pypdf" >nul 2>nul
if errorlevel 1 (
  echo Installing the free dependencies. Internet is required for this first setup.
  ".venv\Scripts\python.exe" -m pip install -r requirements.txt
  if errorlevel 1 (
    echo Dependency installation failed. Check your internet connection and retry.
    pause
    exit /b 1
  )
)
if /i "%~1"=="--setup-only" exit /b 0
echo.
echo Open http://127.0.0.1:5050 in your browser.
echo Keep this window open while using the workspace.
echo.
".venv\Scripts\python.exe" app.py
pause
