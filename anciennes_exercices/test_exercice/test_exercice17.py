import pytest

def trouver_minimum(nombres):
    if not isinstance (nombres, list):
        raise TypeError
    elif nombres == []:
        raise ValueError
    else:
        return min(nombres)

def test_erreur_type():
    with pytest.raises(TypeError):
        trouver_minimum(123)

def test_erreur_valeur():
    with pytest.raises(ValueError):
        trouver_minimum([])

def test_cas_normal():
    assert trouver_minimum([10, 4, 25]) == 4