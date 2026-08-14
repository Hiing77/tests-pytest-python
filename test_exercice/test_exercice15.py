import pytest

def calculer_somme(nombres):
    if not isinstance (nombres, (list)):
        raise TypeError
    
    return sum(nombres)


def test_liste_normale():
    assert calculer_somme([1, 2, 3, 4]) == 10

def test_liste_vide():
    assert calculer_somme([]) == 0

def test_erreur_type(): 
    with pytest.raises(TypeError):
        calculer_somme(123)