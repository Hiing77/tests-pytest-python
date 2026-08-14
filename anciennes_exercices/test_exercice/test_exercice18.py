import pytest

def calculer_aire_rectangle(longueur, largeur):
    if not isinstance (largeur,(int, float)):
        raise TypeError

    if not isinstance (longueur,(int, float)):
        raise TypeError

    elif longueur <= 0 or largeur <= 0:
        raise ValueError

    else:
        return longueur * largeur

def test_erreur_type():
    with pytest.raises(TypeError):
        calculer_aire_rectangle("AZE")

def test_erreur_valeur():
    with pytest.raises(ValueError):
        calculer_aire_rectangle(0, 5)

def test_calcul_normal():
    assert calculer_aire_rectangle(4, 5) == 20