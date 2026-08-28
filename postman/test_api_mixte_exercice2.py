import pytest
import requests

@pytest.fixture
def statut_attendu():
    return 200

@pytest.mark.parametrize("id_album, userId_attendu",[
(1, 1),
(5, 1),
(11, 2)
])

def test_recuperer_album_mixte(id_album, userId_attendu, statut_attendu)
    url = f"https://jsonplaceholder.typicode.com/albums/){id_album}"
    reponse = requests.post(url)

    assert reponse.status_code == 200

    donnees = reponse.json()
    assert donnees["userId"] == userId_attendu