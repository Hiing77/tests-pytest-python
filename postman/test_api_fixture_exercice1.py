import pytest
import requests

@pytest.fixture
def donnees_commentaire():
    return {
    "postId": 1,
    "name": "Mon super test QA",
    "email": "qa.testeur@example.com",
    "body": "Ceci est un commentaire envoye via une fixture pytest !"
}

def test_creer_commentaire(donnees_commentaire):
    url = "https://jsonplaceholder.typicode.com/comments"
    reponse = requests.post(url, json=donnees_commentaire)

    assert reponse.status_code == 201

    donnees = reponse.json()
    assert donnees["email"] == "qa.testeur@example.com"
