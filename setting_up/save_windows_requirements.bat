@echo off
if not exist env_requirements\windows (
  ECHO Creating folder
  MKDIR env_requirements\windows
)

ECHO Saving windows conda env requirements
%windir%\system32\cmd.exe "/c conda activate anymind && conda env export > env_requirements\windows\conda.yml"

ECHO Saving windows conda env requirements without build version
%windir%\system32\cmd.exe "/c conda activate anymind && conda env export --no-builds > env_requirements\windows\conda_no_builds.yml"

ECHO Saving windows pip requirements
%windir%\system32\cmd.exe "/c conda activate anymind && pip freeze > env_requirements\windows\pip.txt"

ECHO Done saving windows env requirements
PAUSE