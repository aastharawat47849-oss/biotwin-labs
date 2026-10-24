@echo off
title BioTwin Labs - Precision Longevity Platform
echo ===================================================
echo     STARTING BIOTWIN LABS LOCAL WEB SERVER...
echo ===================================================
echo.
echo Opening Portal at http://127.0.0.1:5050 in 3 seconds...
timeout /t 3 /nobreak >nul
start http://127.0.0.1:5050
python "%~dp0web\app.py"
pause
