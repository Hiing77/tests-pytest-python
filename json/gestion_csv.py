import csv
import os

dossier_script = os.path.dirname(os.path.abspath(__file__))
chemin_csv = os.path.join(dossier_script, "gestion_csv.csv")

tests = [
    ["ID_Test", "Fonctionnalite", "Statut_Attendu"],
    ["TC001", "Connexion", "Succes"],
    ["TC002", "Mot de passe oublie", "Succes"],
    ["TC003", "Panier d'achat", "Echec"],
]

with open(chemin_csv, "w", newline="", encoding="utf-8") as fichier:
  writer = csv.writer(fichier)
  writer.writerows(tests)

print(f"Fichier CSV créé ici : {chemin_csv}")

print("\n--- Lecture du fichier CSV ---")
with open(chemin_csv, "r", encoding="utf-8") as fichier:
  lecteur = csv.reader(fichier)
  for ligne in lecteur:
    print(ligne)

print("\n--- Liste des tests en échec ---")
with open(chemin_csv, "r", encoding="utf-8") as fichier:
    lecteur = csv.reader(fichier)
    
    next(lecteur) 
    
    for ligne in lecteur:
        if ligne[2] == "Echec":
            print(f"Test critique détecté : {ligne[0]} - {ligne[1]}")