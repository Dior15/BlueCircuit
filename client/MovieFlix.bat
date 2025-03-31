@echo off
@REM Change this to your BlueCircuit directory
cd /d ""
start cmd /k "client/app.py"
timeout /t 2 >nul
start "" "http://127.0.0.1:5000"
exit