@echo off
echo Installing dependencies for Kosaco ScoutMe...
py -m pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Error installing dependencies. Please ensure Python and PIP are installed and in your PATH.
    pause
) else (
    echo.
    echo Dependencies installed successfully.
    pause
)
