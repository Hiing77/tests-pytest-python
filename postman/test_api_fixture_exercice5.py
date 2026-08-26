import pytest  
import requests

@pytest.fixture
def donnees_todo():
    return {
    "userId": 3,
    "title": "Apprendre les fixtures avec pytest",
    "completed": False
}

def test_creer_todo(donnees_todo):
    url = "https://jsonplaceholder.typicode.com/todos"
    reponse = requests.post(url, json=donnees_todo)

    assert reponse.status_code == 201

    donnees = reponse.json()
    assert donnees["title"] == "Apprendre les fixtures avec pytest"


