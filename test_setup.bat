@echo off
REM This script sets the PYTHONPATH to include the src directory on Windows

REM Get the current directory (repository root)
SET REPO_ROOT=%CD%

REM Append the src/ directory to PYTHONPATH
SET PYTHONPATH=%PYTHONPATH%;%REPO_ROOT%\src

REM Display the new PYTHONPATH to confirm
echo PYTHONPATH has been set to include %REPO_ROOT%\src