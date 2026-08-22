
import pytest
import requests

@pytest.fixture
def data_utilisateur():
    return (7, "Kurtis Weissnat")

def test_id_a_tester(data_utilisateur):
    user_id, nom_attendu = data_utilisateur
    
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    reponse = requests.get(url)
    
    assert reponse.status_code == 200
    
    donnees = reponse.json()
    assert donnees["name"] == nom_attendu