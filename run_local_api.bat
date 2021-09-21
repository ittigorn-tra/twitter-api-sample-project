@echo off
%windir%\system32\cmd.exe "/c conda activate anymind && uvicorn app.main:app --port 80 --reload"