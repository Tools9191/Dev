import re

# Variables pour stocker les valeurs
variables = {}

# Fonction pour exécuter une ligne de code
def execute_line(line):
    # Déclaration de variable
    let_pattern = r"let\s+(\w+)\s*=\s*(\S+)"
    match = re.match(let_pattern, line)
    if match:
        var_name, value = match.groups()
        if value.isdigit():
            variables[var_name] = int(value)
        else:
            variables[var_name] = value
        return

    # Affichage
    if line.startswith("print"):
        message = line[5:].strip()  # Récupérer le message après 'print'
        print(message)

# Fonction principale pour exécuter un fichier .DST
def execute_file(file_path):
    with open(file_path, "r") as file:
        code = file.read()
        for line in code.split("\n"):
            execute_line(line)

# Exemple d'utilisation
execute_file("script.dst")  # Remplace "script.dst" par le chemin de ton fichier DevStorm
