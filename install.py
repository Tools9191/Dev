import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
import shutil
import time
import urllib.request
import zipfile
import subprocess
from win32com.client import Dispatch  # Nécessaire pour créer des raccourcis

class InstallateurApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Installation de StormDev-X")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.step = 0  # Pour gérer les étapes de l'installation

        # Modifier le chemin pour installer dans "C:\Users\Storm\AppData\Local\Programs"
        self.install_dir = os.path.join(os.environ["LOCALAPPDATA"], "Programs", "StormDev-X")

        # Créer le dossier "Programs" et "StormDev-X" si nécessaire
        if not os.path.exists(self.install_dir):
            os.makedirs(self.install_dir)

        # Répertoire Dev-main sur le bureau
        self.desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
        self.dev_main_dir = os.path.join(self.desktop, "Dev-main")  # Répertoire Dev-main sur le bureau

        # Créer les éléments de l'interface
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Bienvenue dans l'installation de StormDev-X", font=("Helvetica", 16, "bold"), fg="#4A90E2")
        self.title_label.pack(pady=20)

        # Etiquette de progress
        self.progress_label = tk.Label(self.root, text="Préparation de l'installation...", font=("Arial", 12))
        self.progress_label.pack(pady=10)

        # Barre de progression
        self.progress = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress, maximum=100, length=350)
        self.progress_bar.pack(pady=20)

        # Étape actuelle
        self.step_label = tk.Label(self.root, text="Étape 1 sur 5", font=("Arial", 10))
        self.step_label.pack(pady=5)

        # Options supplémentaires pendant l'installation
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(pady=10)

        self.checkbox_var = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.options_frame, text="Installer StormDev-X dans le menu Démarrer", variable=self.checkbox_var)
        self.checkbox.pack()

        self.next_button = tk.Button(self.root, text="Suivant", command=self.next_step, font=("Arial", 12), bg="#4A90E2", fg="white", relief="raised")
        self.next_button.pack(pady=10)

    def update_progress(self, value):
        self.progress.set(value)
        self.root.update_idletasks()

    def afficher_message(self, message):
        messagebox.showinfo("Installation", message)

    def install_git(self):
        """Installe Git en mode silencieux."""
        try:
            self.update_progress(10)
            self.progress_label.config(text="Vérification de l'installation de Git...")
            time.sleep(1)
            
            # Vérifier si Git est déjà installé
            git_check = shutil.which("git")
            if git_check:
                self.update_progress(20)
                self.progress_label.config(text="Git déjà installé...")
            else:
                self.update_progress(20)
                self.progress_label.config(text="Installation de Git en cours...")
                
                # Télécharger le fichier d'installation de Git pour Windows
                git_installer_url = "https://cold5.gofile.io/download/web/d0eb4284-196d-4d53-af05-acee61f01ba0/Git-2.47.1.2-64-bit.exe"  # Exemple avec version stable
                git_installer_path = os.path.join(self.install_dir, "Git-2.47.1.2-64-bit.exe")
                
                # Télécharger l'installateur Git
                urllib.request.urlretrieve(git_installer_url, git_installer_path)
                
                # Exécuter l'installation silencieuse de Git
                subprocess.run([git_installer_path, "/VERYSILENT", "/NORESTART"], check=True)
                
                # Supprimer l'installateur après l'installation
                os.remove(git_installer_path)
                
                self.update_progress(40)
                self.progress_label.config(text="Git installé avec succès !")
            
        except Exception as e:
            self.afficher_message(f"Erreur lors de l'installation de Git : {str(e)}")

    def download_and_extract_zip(self, url, install_dir):
        try:
            self.update_progress(50)
            self.progress_label.config(text="Vérification du dossier d'installation...")
            time.sleep(1)
            
            if os.path.exists(install_dir):
                self.update_progress(60)
                self.progress_label.config(text="Dossier existant trouvé, suppression en cours...")
                shutil.rmtree(install_dir)
            
            os.makedirs(install_dir, exist_ok=True)
            self.update_progress(70)
            self.progress_label.config(text="Dossier d'installation créé...")
            
            zip_path = os.path.join(install_dir, "StormDev-X.zip")
            self.update_progress(80)
            self.progress_label.config(text="Téléchargement du fichier...")
            
            # Télécharger le fichier zip à partir du lien GitHub
            urllib.request.urlretrieve("https://github.com/Tools9191/Dev/archive/refs/heads/main.zip", zip_path)
            
            self.update_progress(90)
            self.progress_label.config(text="Extraction du fichier ZIP...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(install_dir)
            
            os.remove(zip_path)
            
            self.update_progress(100)
            self.progress_label.config(text="Installation terminée !")
            self.afficher_message("StormDev-X a été installé avec succès !")
            
        except Exception as e:
            self.afficher_message(f"Erreur pendant l'installation : {str(e)}")

    def next_step(self):
        if self.step == 0:
            self.step += 1
            self.step_label.config(text="Étape 2 sur 5")
            self.progress_label.config(text="Installation de Git...")
            self.update_progress(10)
            self.install_git()  # Installer Git d'abord
        elif self.step == 1:
            self.step += 1
            self.step_label.config(text="Étape 3 sur 5")
            self.progress_label.config(text="Préparation pour le téléchargement...")
            self.update_progress(30)
            time.sleep(1)

            # Télécharger et extraire le fichier .zip à partir du lien GitHub
            self.download_and_extract_zip("https://github.com/Tools9191/Dev/archive/refs/heads/main.zip", self.install_dir)
        elif self.step == 2:
            self.step += 1
            self.step_label.config(text="Étape 4 sur 5")
            self.progress_label.config(text="Configuration du menu Démarrer...")
            time.sleep(1)
            self.update_progress(80)
            
            if self.checkbox_var.get():
                self.afficher_message("Ajout au menu Démarrer activé !")
            
            self.create_shortcuts()
            self.next_button.config(text="Terminer")
        else:
            self.afficher_message("Installation terminée avec succès!")
            self.root.quit()

    def create_shortcuts(self):
        try:
            # Chemin du fichier editscript.bat à raccourcir
            editscript_bat_path = os.path.join(self.dev_main_dir, "editscript.bat")

            # Créer le raccourci sur le bureau pour editscript.bat
            self.create_shortcut(editscript_bat_path, os.path.join(self.desktop, "editscript.bat.lnk"))

            # Créer le raccourci pour script.dst
            script_dst_path = os.path.join(self.dev_main_dir, "script.dst")
            self.create_shortcut(script_dst_path, os.path.join(self.desktop, "script.dst.lnk"))

        except Exception as e:
            self.afficher_message(f"Erreur lors de la création des raccourcis : {str(e)}")

    def create_shortcut(self, target, shortcut_path):
        """ Crée un raccourci Windows """
        try:
            shell = Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.TargetPath = target
            shortcut.WorkingDirectory = os.path.dirname(target)
            shortcut.IconLocation = target  # Optionnel : définir une icône pour le raccourci
            shortcut.save()
        except Exception as e:
            self.afficher_message(f"Erreur lors de la création du raccourci: {str(e)}")

# Création de la fenêtre Tkinter
root = tk.Tk()
app = InstallateurApp(root)
root.mainloop()
