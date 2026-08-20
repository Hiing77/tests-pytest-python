import json
import os

dossier_script = os.path.dirname(os.path.abspath(__file__))
chemin_json = os.path.join(dossier_script, "exercice_json.json")

utilisateurs_test = [
    {
        "id": "P001", 
        "nom": "Casque Audio",
        "prix": 45,
        "en_stock": True,
    },
    {
        "id": "P002",
        "nom": "Clavier Gamer",
        "prix": 80,
        "en_stock": False,
    },
    {
        "id": "P003",
        "nom": "Souris Sans Fil",
        "prix": 25,
        "en_stock": True,
    },
]

with open(chemin_json, "w", encoding="utf-8") as fichier:
  json.dump(utilisateurs_test, fichier, indent=4, ensure_ascii=False)

print(f"Fichier créé ici : {chemin_json}")

with open(chemin_json, "r", encoding="utf-8") as fichier:
  donnees_lues = json.load(fichier)

  print("\n--- Utilisateurs actifs ---")
  for utilisateur in donnees_lues:
    if utilisateur["en_stock"] is True:
      print(f"- {utilisateur['nom']}")