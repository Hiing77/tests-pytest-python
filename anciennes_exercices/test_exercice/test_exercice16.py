import pytest

def trouver_maximum(nombres) :
    if not isinstance (nombres, list):
        raise TypeError
    
    elif nombres == []:
        raise ValueError
    
    else:
        return max(nombres)

def test_erreur_type():
    with pytest.raises(TypeError):
        trouver_maximum(123)

def test_erreur_valeur():
    with pytest.raises(ValueError):
        trouver_maximum([])

def test_cas_normal():
    assert trouver_maximum([2, 8, 5]) == 8