import pytest
import requests

@pytest.fixture
def headers_communs():
    return {
      "Content-Type": "application/json",
      "User-Agent": "TesteurQA-Apprenant"
    }

def test_avec_headers(headers_communs):
    url = "https://jsonplaceholder.typicode.com/todos/1"
    reponse = requests.get(url, headers=headers_communs)
    
    assert reponse.status_code == 200
    donnees = reponse.json()
    assert donnees["id"] == 1