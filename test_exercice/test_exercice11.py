import pytest

def calculer_cube(n):
    if not isinstance (n,(int,float)):
        raise TypeError

    elif n < 0:
        raise ValueError

    else:
        return n ** 3


def test_erreur_type():
    with pytest.raises(TypeError):
        calculer_cube("AZE")


def test_erreur_valeur():
    with pytest.raises(ValueError):
        calculer_cube(-6)


def test_cas_normal():
    assert calculer_cube(3) == 27