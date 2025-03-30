@echo off
@REM Change this to your BlueCircuit directory
cd /d "C:\Users\Elllycea\OntarioTech\csci2040u\BlueCircuit\client"
start cmd /k "C:\Users\Elllycea\AppData\Local\Programs\Python\Python310\python.exe app.py"
timeout /t 2 >nul
start "" "http://127.0.0.1:5000"
exit