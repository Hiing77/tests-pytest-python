import pytest
import requests

@pytest.fixture
def statut_attendu():
    return 200

@pytest.mark.parametrize("id_user,ville_attendue",[
    (1, "Gwenborough"),
    (2, "Wisokyburgh")
])

def test_recuperer_user_mixte(statut_attendu, id_user, ville_attendue):
    url = f"https://jsonplaceholder.typicode.com/users/{id_user}"
    reponse = requests.get(url)

    assert reponse.status_code == statut_attendu

    donnees = reponse.json()

    assert donnees["address"]["city"] == ville_attendue