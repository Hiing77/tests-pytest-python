import requests
import pytest

def test_recuperer_post():
    # 1. On envoie une requête GET vers une API publique de test
    url = "https://jsonplaceholder.typicode.com/posts/1"
    reponse = requests.get(url)
    
    # 2. On vérifie que le code de statut HTTP est 200 (Succès)
    assert reponse.status_code == 200
    
    # 3. On convertit la réponse en JSON et on vérifie une donnée
    donnees = reponse.json()
    assert donnees["id"] == 1
    assert "title" in donnees
    
    print("Données récupérées avec succès :", donnees["title"])
    