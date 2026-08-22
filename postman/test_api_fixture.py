import pytest
import requests

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

def test_recuperer_utilisateurs(base_url):
    url_complete = f"{base_url}/users"
    
    reponse = requests.get(url_complete)
    
    assert reponse.status_code == 200
    print("Utilisateurs récupérés avec succès via la fixture !")