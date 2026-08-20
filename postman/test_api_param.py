import requests
import pytest

@pytest.mark.parametrize("id_post, statut_attendu", [
    (1, 200),
    (9999, 404)  
])
def test_recuperer_posts_avec_statut(id_post, statut_attendu):
    url = f"https://jsonplaceholder.typicode.com/posts/{id_post}"
    reponse = requests.get(url)
    
    
    assert reponse.status_code == statut_attendu