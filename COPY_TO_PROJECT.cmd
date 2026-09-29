@echo off
setlocal
cd /d "%~dp0"

echo RowletAI - menjalankan aplikasi lokal
echo.

if not exist ".venv\Scripts\python.exe" (
    echo Environment Python belum tersedia.
    echo Ikuti langkah instalasi di README.md terlebih dahulu.
    pause
    exit /b 1
)

".venv\Scripts\python.exe" -m streamlit run "app\dashboard.py"
if errorlevel 1 pause
