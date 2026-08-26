import pytest
import requests

@pytest.fixture
def id_a_supprimer():
    return { 
        5
}

def test_supprimer_post(id_a_supprimer):
    url = f"https://jsonplaceholder.typicode.com/posts/{id_a_supprimer}"
    reponse = requests.delete(url)

    assert reponse.status_code == 200


    
