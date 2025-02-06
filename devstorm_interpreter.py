@echo off
:: Vérifier si Python est installé
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python n'est pas installé ou n'est pas dans le PATH.
    pause
    exit /b
)

:: Chemin d'accès vers StormDev-X pour différents utilisateurs
set stormDevXPath="%USERPROFILE%\AppData\Local\Programs\StormDev-X"

:: Aller dans le répertoire StormDev-X
cd /d %stormDevXPath%
if exist devstorm_interpreter.py (
    echo Lancement de devstorm_interpreter.py dans StormDev-X...
    python devstorm_interpreter.py
) else (
    echo Le fichier devstorm_interpreter.py n'a pas été trouvé dans %stormDevXPath%.
)

:: Chemin d'accès vers Dev-main
set devMainPath="%USERPROFILE%\AppData\Local\Programs\StormDev-X\Dev-main"

:: Aller dans le répertoire Dev-main
cd /d %devMainPath%
if exist devstorm_interpreter.py (
    echo Lancement de devstorm_interpreter.py dans Dev-main...
    python devstorm_interpreter.py
) else (
    echo Le fichier devstorm_interpreter.py n'a pas été trouvé dans %devMainPath%.
)

:: Message de fin
echo Le script a été lancé dans les répertoires si les fichiers étaient présents.
pause
