@echo off
%windir%\system32\cmd.exe "/c conda activate anymind && pytest"
PAUSE