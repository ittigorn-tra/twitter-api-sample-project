@echo off
%windir%\system32\cmd.exe "/c conda activate twitter-api-sample-project && uvicorn app.main:app --port 80 --reload"