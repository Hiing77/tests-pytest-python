import pytest
import requests

@pytest.mark.parametrize("id_photo, albumId_attendu",[
    (1, 1),
    (50, 1),
    (100, 2)
])

def test_recuperer_photo(id_photo, albumId_attendu):
    url = f"https://jsonplaceholder.typicode.com/photos/{id_photo}"
    reponse = requests.get(url)

    assert reponse.status_code == 200

    donnees = reponse.json()
    assert donnees["albumId"] == albumId_attendu