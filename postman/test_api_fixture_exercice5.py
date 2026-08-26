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
    url = f"https://jsonplaceholder.typicode.com/todos"
    reponse = requests.post(url)

    donnees = reponse.json()
    reponse = donnees["title"] == "Apprendre les fixtures avec pytest"


