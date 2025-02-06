import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
import shutil
import time
import urllib.request
import zipfile

class InstallateurApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Installation de StormDev-X")
        self.root.geometry("500x350")
        self.root.resizable(False, False)
        
        self.step = 0  # Pour gérer les étapes de l'installation
        self.install_dir = "C:\\Users\\Storm\\AppData\\Local\\Programs\\StormDev-X"
        
        self.create_widgets()
    
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Bienvenue dans l'installation de StormDev-X", font=("Arial", 14), fg="blue")
        self.title_label.pack(pady=20)
        
        # Etiquette de progress
        self.progress_label = tk.Label(self.root, text="Préparation de l'installation...", font=("Arial", 12))
        self.progress_label.pack(pady=10)
        
        # Barre de progression
        self.progress = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress, maximum=100, length=350)
        self.progress_bar.pack(pady=20)
        
        # Étape actuelle
        self.step_label = tk.Label(self.root, text="Étape 1 sur 4", font=("Arial", 10))
        self.step_label.pack(pady=5)
        
        # Options supplémentaires pendant l'installation
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(pady=10)
        
        self.checkbox_var = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.options_frame, text="Installer StormDev-X dans le menu Démarrer", variable=self.checkbox_var)
        self.checkbox.pack()

        self.next_button = tk.Button(self.root, text="Suivant", command=self.next_step, font=("Arial", 12))
        self.next_button.pack(pady=10)
    
    def update_progress(self, value):
        self.progress.set(value)
        self.root.update_idletasks()

    def afficher_message(self, message):
        messagebox.showinfo("Installation", message)

    def download_and_extract_zip(self, url, install_dir):
        try:
            self.update_progress(10)
            self.progress_label.config(text="Vérification du dossier d'installation...")
            time.sleep(1)
            
            if os.path.exists(install_dir):
                self.update_progress(20)
                self.progress_label.config(text="Dossier existant trouvé, suppression en cours...")
                shutil.rmtree(install_dir)
            
            os.makedirs(install_dir, exist_ok=True)
            self.update_progress(30)
            self.progress_label.config(text="Dossier d'installation créé...")
            
            zip_path = os.path.join(install_dir, "StormDev-X.zip")
            self.update_progress(40)
            self.progress_label.config(text="Téléchargement du fichier...")
            urllib.request.urlretrieve(url, zip_path)
            
            self.update_progress(60)
            self.progress_label.config(text="Extraction du fichier ZIP...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(install_dir)
            
            os.remove(zip_path)
            
            self.update_progress(80)
            self.progress_label.config(text="Installation terminée !")
            self.afficher_message("StormDev-X a été installé avec succès !")
            self.update_progress(100)
            
        except Exception as e:
            self.afficher_message(f"Erreur pendant l'installation : {str(e)}")

    def next_step(self):
        if self.step == 0:
            self.step += 1
            self.step_label.config(text="Étape 2 sur 4")
            self.progress_label.config(text="Préparation pour le téléchargement...")
            self.update_progress(20)
            time.sleep(1)
            self.download_and_extract_zip("https://github.com/Tools9191/Dev/archive/refs/heads/main.zip", self.install_dir)
        elif self.step == 1:
            self.step += 1
            self.step_label.config(text="Étape 3 sur 4")
            self.progress_label.config(text="Configuration du menu Démarrer...")
            time.sleep(1)
            self.update_progress(80)
            # Ajouter des fonctionnalités comme ajouter dans le menu Démarrer ici...
            if self.checkbox_var.get():
                self.afficher_message("Ajout au menu Démarrer activé !")
            self.next_button.config(text="Terminer")
        else:
            self.afficher_message("Installation terminée avec succès!")
            self.root.quit()


# Création de la fenêtre Tkinter
root = tk.Tk()
app = InstallateurApp(root)
root.mainloop()
