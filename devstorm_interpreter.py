import os
import re
import win32com.client

# Dictionnaire pour stocker les variables
variables = {}

# Fonction pour exécuter une ligne de code
def execute_line(line):
    # Déclaration de variable (let)
    let_pattern = r"let\s+(\w+)\s*=\s*(\S+)"
    match = re.match(let_pattern, line)
    if match:
        var_name, value = match.groups()
        # Si la valeur est un nombre, on la convertit en entier
        if value.isdigit():
            variables[var_name] = int(value)
        else:
            variables[var_name] = value
        return

    # Affichage avec 'print'
    if line.startswith("print"):
        message = line[5:].strip()  # Récupérer le message après 'print'
        # Remplacer les variables dans le message par leurs valeurs
        for var in variables:
            message = message.replace(var, str(variables[var]))
        print(message)

    # Gestion des conditions 'if'
    if line.startswith("if"):
        condition = line[2:].strip()
        if eval(condition, {}, variables):
            return True
        else:
            return False

    # Boucle 'while'
    if line.startswith("while"):
        condition = line[5:].strip()
        while eval(condition, {}, variables):
            pass  # Implémentation de la boucle en fonction de l'interprétation

# Fonction principale pour exécuter un fichier .DST
def execute_file(file_path):
    try:
        # Ouvre le fichier .DST et le lit ligne par ligne
        with open(file_path, "r") as file:
            code = file.read()
            for line in code.split("\n"):
                execute_line(line)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Fonction pour créer un raccourci vers le fichier script.dst sur le bureau
def create_shortcut(file_path):
    try:
        user_folder = os.path.expanduser("~")  # Récupère le répertoire de l'utilisateur
        desktop_path = os.path.join(user_folder, "Desktop")
        shortcut_name = "script_dst.lnk"

        # Créer le raccourci
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortcut(os.path.join(desktop_path, shortcut_name))
        shortcut.TargetPath = file_path
        shortcut.WorkingDirectory = os.path.dirname(file_path)  # Facultatif : définit le répertoire de travail
        shortcut.Save()

        print(f"Raccourci créé sur le bureau : {os.path.join(desktop_path, shortcut_name)}")
    except Exception as e:
        print(f"Erreur lors de la création du raccourci : {e}")

# Exemple d'utilisation : obtenir dynamiquement le chemin du fichier .DST
user_folder = os.path.expanduser("~")  # Cela récupère le répertoire de l'utilisateur actuel
file_path = os.path.join(user_folder, "AppData", "Local", "Programs", "StormDev-X", "Dev-main", "script.dst")

# Créer un raccourci vers script.dst sur le bureau
create_shortcut(file_path)

# Exécuter le fichier .DST
execute_file(file_path)
