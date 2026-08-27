import pytest
import requests

@pytest.fixture
def statut_attendu():
    return 200

@pytest.mark.parametrize("id_utilisateur, nom_attendu"[
    (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch")
])

def test_recuperer_utilisateur_mixte(statut_attendu, id_utilisateur, nom_attendu):
    url = f"https://jsonplaceholder.typicode.com/users/"
    reponse = requests.get(url, json=statut_attendu, json=id_utilisateur, json=nom_attendu)
    