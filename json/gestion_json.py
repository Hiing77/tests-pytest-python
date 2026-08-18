import json
import os # 1. On importe le module pour gérer les chemins

# 2. On récupère le dossier où se trouve le script
dossier_script = os.path.dirname(os.path.abspath(__file__))
# 3. On crée le chemin complet vers le fichier JSON
chemin_json = os.path.join(dossier_script, "gestion_json.json")

test = {
    "id": "TC001",
    "nom": "Ratta",
    "email": "supiii77@hotmail.com",
    "actif": False,
}

# 4. On utilise cette variable 'chemin_json' pour ouvrir le fichier
with open(chemin_json, "w", encoding="utf-8") as fichier:
    json.dump(test, fichier, indent=4, ensure_ascii=False)

print(f"Fichier créé ici : {chemin_json}")

with open(chemin_json, "r", encoding="utf-8") as fichier:
  donnees_lues = json.load(fichier)
  # Afficher l'email récupéré
  print("Email récupéré du JSON :", donnees_lues["email"])


