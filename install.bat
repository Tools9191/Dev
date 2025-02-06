::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAnk
::fBw5plQjdG8=
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSDk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFChAQxaPAE+1EbsQ5+n//Na0tkIPWcY6bsLjl+XAcK0FvBGqcI4otg==
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
:: Vérifie si Python est installé
where python >nul 2>nul
if errorlevel 1 (
    echo Python n'est pas installé ou n'est pas dans le PATH.
    pause
    exit /b
)

:: Récupère le dossier AppData de l'utilisateur actuel
set "appdata_folder=%APPDATA%"

:: Crée le chemin complet vers le dossier d'installation
set "install_dir=%appdata_folder%\..\Local\Programs\StormDev-X\Dev-main"

:: Change le répertoire pour se placer dans le dossier contenant le script Python
cd /d "%install_dir%"

:: Exécute le script Python install.py
python install.py

:: Pause pour voir les résultats avant de fermer
pause
