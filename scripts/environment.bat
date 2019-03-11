@echo off
call conda-env create --file ../anaconda_env.yml
if %errorlevel% neq 0 ( 
    echo [ERROR]: Something wrong happened during the creation of the environment.
    exit /b %ERRORLEVEL%
    ) else (
        activate aiworkshop
    )
