import pytest
import requests

@pytest.mark.parametrize("id_post, userId_attendu",[
    (1, 1),
    (6, 1),
    (11, 2)
])

def test_recuperer_post_user(id_post, userId_attendu):
    url = f"https://jsonplaceholder.typicode.com/posts/{id_post}"
    reponse = requests.get(url)

    assert reponse.status_code == 200

    donnees = reponse.json()
    assert donnees["userId"] == userId_attendu

