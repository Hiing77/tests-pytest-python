import pytest
import requests

@pytest.fixture
def statut_attendu():
    return 200

@pytest.mark.parametrize("id_post, userId_attendu",[
    (1, 1),
    (10, 1),
    (11, 2)
])

def test_recuperer_post_mixte(statut_attendu, id_post, userId_attendu):
    url = f"https://jsonplaceholder.typicode.com/posts/{id_post}"
    reponse = requests.get(url)

    assert reponse.status_code == statut_attendu

    donnees = reponse.json()
    assert donnees["userId"] == userId_attendu
