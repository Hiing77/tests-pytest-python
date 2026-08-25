import pytest   
import requests

@pytest.fixture
def donnees_album():
    return {
    "userId": 7,
    "title": "Mes photos de vacances QA"
}

def test_creer_album(donnees_album):
    url = "https://jsonplaceholder.typicode.com/albums"
    reponse = requests.post(url, json=donnees_album)

    assert reponse.status_code == 201

    donnees = reponse.json()
    assert donnees["title"] == "Mes photos de vacances QA"
    