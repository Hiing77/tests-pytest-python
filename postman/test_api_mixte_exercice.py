import pytest
import requests

@pytest.fixture
def statut_attendu():
    return 200

@pytest.mark.parametrize("id_utilisateur, nom_attendu",[
    (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch")
])

def test_recuperer_utilisateur_mixte(statut_attendu, id_utilisateur, nom_attendu):
    url = f"https://jsonplaceholder.typicode.com/users/{id_utilisateur}"
    reponse = requests.get(url)

    assert reponse.status_code == 200

    donnees = reponse.json()
    assert donnees["name"] == nom_attendu