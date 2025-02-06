@echo off
:: Vérifie si Python est installé
where python >nul 2>nul
if errorlevel 1 (
    echo Python n'est pas installé ou n'est pas dans le PATH.
    pause
    exit /b
)

:: Récupère le dossier Desktop de l'utilisateur actuel
set "desktop_folder=%USERPROFILE%\Desktop"

:: Crée le chemin complet vers le dossier d'installation
set "install_dir=%desktop_folder%\Dev-main"

:: Change le répertoire pour se placer dans le dossier contenant le script Python
cd /d "%install_dir%"

:: Exécute le script Python install.py
python install.py

:: Pause pour voir les résultats avant de fermer
pause
