import pytest

def calculer_perimetre_rectangle(longueur, largeur):
    if not isinstance (longueur, (int, float)):
        raise TypeError
    if not isinstance (largeur, (int, float)):
        raise TypeError

    elif longueur <= 0 or largeur <= 0:
        raise ValueError

    else:
        return 2 * (longueur + largeur)

def test_erreur_type():
    with pytest.raises(TypeError):
        calculer_perimetre_rectangle("AAZE")


def test_erreur_valeur():
    with pytest.raises(ValueError):
        calculer_perimetre_rectangle(5,-1)


def test_calcul_normal():
    assert calculer_perimetre_rectangle(4, 5) == 18