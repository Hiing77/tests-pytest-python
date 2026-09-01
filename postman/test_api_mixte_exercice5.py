import pytest
import requests

@pytest.fixture
def statut_attendu():
    return 200

@pytest.mark.parametrize("id_todo,completed_attendu",[
    (1, False),
    (2, False),
    (4, True)
])

def test_recuperer_todo_mixte(statut_attendu, id_todo, completed_attendu):
    url = f"https://jsonplaceholder.typicode.com/todos/{id_todo}"
    reponse = requests.get(url)

    assert reponse.status_code == statut_attendu

    donnees = reponse.json()
    donnees["completed"] == completed_attendu