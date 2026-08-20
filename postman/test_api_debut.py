import requests
import pytest

def test_recuperer_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    reponse = requests.get(url)
    
    assert reponse.status_code == 200
    
    donnees = reponse.json()
    assert donnees["id"] == 1
    assert "title" in donnees
    
    print("Données récupérées avec succès :", donnees["title"])
    