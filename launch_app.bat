@echo off
setlocal
color 0a

echo ========================================
echo Second-Hand Vehicle Price Forecasting
echo ========================================
echo.

REM 1) Crear entorno virtual si no existe
if not exist ".venv\Scripts\python.exe" (
    echo [1/4] Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo Error: could not create the virtual environment.
        pause
        exit /b 1
    )
) else (
    echo [1/4] Virtual environment already exists.
)

REM 2) Activar entorno virtual
echo [2/4] Activating virtual environment...
call .venv\Scripts\activate
if errorlevel 1 (
    echo Error: could not activate the virtual environment.
    pause
    exit /b 1
)

REM 3) Comprobar dependencias clave
echo [3/4] Checking dependencies...
python -c "import pandas, sklearn, matplotlib, seaborn, joblib, streamlit, xgboost, catboost, jupyter" >nul 2>nul

if errorlevel 1 (
    echo Some dependencies are missing. Installing from requirements.txt...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: dependency installation failed.
        pause
        exit /b 1
    )
) else (
    echo All dependencies are already installed.
)

REM 4) Lanzar Streamlit
echo [4/4] Launching Streamlit application...
streamlit run app/streamlit_app.py

pause
endlocal