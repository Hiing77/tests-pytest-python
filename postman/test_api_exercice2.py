import requests
import pytest

@pytest.mark.parametrize("id", [2, 4, 6])

def test_recuperer_id(id):
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    reponse = requests.get(url)

    assert reponse.status_code == 200
    
    donnees = reponse.json()
    assert donnees["id"] == id
