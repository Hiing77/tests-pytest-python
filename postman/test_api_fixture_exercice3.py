import pytest
import requests

@pytest.fixture
def donnees_mise_a_jour():
	return {
    "id": 1,
    "title": "Mon titre modifie via fixture",
    "body": "Ceci est le nouveau contenu mis a jour pour le test QA.",
    "userId": 1
}

def test_modifier_post(donnees_mise_a_jour):
	url = "https://jsonplaceholder.typicode.com/posts/1"
	reponse = requests.put(url, json=donnees_mise_a_jour)
	
	assert reponse.status_code == 200

	donnees = reponse.json()
	assert donnees["title"] == "Mon titre modifie via fixture"
	

 
