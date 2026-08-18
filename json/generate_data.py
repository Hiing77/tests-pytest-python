import json
import os

dossier_script = os.path.dirname(os.path.abspath(__file__))
chemin_json = os.path.join(dossier_script, "generate_data.json")

utilisateurs_test = [
    {
        "id": "TC001",
        "nom": "Alice",
        "email": "alice.test@example.com",
        "actif": True,
    },
    {
        "id": "TC002",
        "nom": "Bob",
        "email": "bob.test@example.com",
        "actif": False,
    },
    {
        "id": "TC003",
        "nom": "Charlie",
        "email": "charlie.test@example.com",
        "actif": True,
    },
]


with open(chemin_json, "w", encoding="utf-8") as fichier:
  json.dump(utilisateurs_test, fichier, indent=4, ensure_ascii=False)

print(f"Fichier créé ici : {chemin_json}")


with open(chemin_json, "r", encoding="utf-8") as fichier:
  donnees_lues = json.load(fichier)

  print("\n--- Utilisateurs actifs ---")
  for utilisateur in donnees_lues:
    if utilisateur["actif"] is True:
      print(f"- {utilisateur['nom']}")

