import pytest
import requests

@pytest.mark.parametrize("id_commentaire,postId_attendu",[
    (1, 1),
    (5, 1),
    (10, 2)
])

def test_recuperer_commentaire(id_commentaire, postId_attendu):
    url = f"https://jsonplaceholder.typicode.com/comments/{id_commentaire}"
    reponse = requests.get(url)

    assert reponse.status_code == 200

    donnees = reponse.json()
    assert donnees["postId"] == postId_attendu