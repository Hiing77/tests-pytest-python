import json
def test_utilisateurs():
    with open("utilisateurs.json", "r") as fichier:
        donnees = json.load(fichier)

        assert donnees[0]["nom"] == "Alice"

