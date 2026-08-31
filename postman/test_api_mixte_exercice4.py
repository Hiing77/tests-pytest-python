import requests
import pytest

@pytest.fixture
def email_reference():
    return "Eliseo@gardner.biz"

@pytest.mark.parametrize("id_commentaire",[
    1,
    2,
    3
])

def test_recuperer_commentaire(email_reference, id_commentaire):
    url = f"https://jsonplaceholder.typicode.com/comments/{id_commentaire}"
    reponse = requests.get(url)

    assert reponse.status_code == 200

    donnees = reponse.json()

    assert "email" in donnees

