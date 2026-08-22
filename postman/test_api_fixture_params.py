import pytest
import requests

@pytest.fixture
def params_filtre():
    return {
        "userId": 3
    }

def test_posts_utilisateur_3(params_filtre):
    url = "https://jsonplaceholder.typicode.com/posts"
    reponse = requests.get(url, params=params_filtre)
    assert reponse.status_code == 200

    donnees = reponse.json()
    assert len(donnees) > 0
    