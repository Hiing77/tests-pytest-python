import pytest

def calculer_perimetre_carre(cote):
    if not isinstance (cote, (int, float)):
        raise TypeError
    elif cote <= 0:
        raise ValueError
    else:
        return cote * 4

def test_TypeError():
    with pytest.raises(TypeError):
        calculer_perimetre_carre("AZE")

def test_ValueError():
    with pytest.raises(ValueError):
        calculer_perimetre_carre(0)

def test_Normal():
    assert calculer_perimetre_carre(5) == 20