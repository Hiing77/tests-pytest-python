import requests
import pytest

@pytest.mark.parametrize("id_post", [1, 2, 3])
def test_recuperer_plusieurs_posts(id_post):

    url = f"https://jsonplaceholder.typicode.com/posts/{id_post}"
    
    reponse = requests.get(url)
    
    assert reponse.status_code == 200
    
    donnees = reponse.json()
    assert donnees["id"] == id_post