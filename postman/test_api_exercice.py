import requests
import pytest

@pytest.mark.parametrize("id", [1, 5, 10])

def test_recuperer_id(id):
    url = f"https://jsonplaceholder.typicode.com/todos/{id}"
    reponse = requests.get(url)

    assert reponse.status_code == 200
    
    donnees = reponse.json()
    assert donnees["id"] == id
