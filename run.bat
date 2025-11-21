@echo off
SETLOCAL
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
echo Starting sender...
python sender.py
pause
ENDLOCAL