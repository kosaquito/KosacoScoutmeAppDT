@echo off
echo Building Kosaco ScoutMe Executable...
py build_exe.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Build failed. Please check the error messages above.
    pause
) else (
    echo.
    echo Build successful! Executable is in the dist folder.
    pause
)
