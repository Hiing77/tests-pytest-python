import pytest
import requests

def test_commentaires():
    url = "https://jsonplaceholder.typicode.com/comments"
    
    mes_parametres = {"postId": 1}
    
    reponse = requests.get(url, params=mes_parametres)

    assert reponse.status_code == 200
