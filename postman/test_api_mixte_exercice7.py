import pytest
import requests

@pytest.fixture
def statut_attendu():
    return 200

@pytest.mark.parametrize("id_album, titre_attendu",[
(1, "quidem molestiae enim"),
(2, "sunt qui excepturi placeat culpa")
])

def test_recuperer_titre_album_mixte(statut_attendu, id_album, titre_attendu):
    url = f"https://jsonplaceholder.typicode.com/albums/{id_album}"
    reponse = requests.get(url)

    assert reponse.status_code == statut_attendu

    donnees = reponse.json()
    assert donnees["title"] == titre_attendu