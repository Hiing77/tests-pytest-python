import requests
import pytest

def test_creer_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    nouveau_post = {
        "title": "Test QA",
        "body": "Ceci est un test de création API",
        "userId": 1
    }
    
    reponse = requests.post(url, json=nouveau_post)
    
    assert reponse.status_code == 201
    
    donnees = reponse.json()
    assert donnees["title"] == "Test QA"
    print("\nPost créé avec succès, ID reçu :", donnees["id"])

    