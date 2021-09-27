@echo off
%windir%\system32\cmd.exe "/c conda activate twitter-api-sample-project && pytest"
PAUSE