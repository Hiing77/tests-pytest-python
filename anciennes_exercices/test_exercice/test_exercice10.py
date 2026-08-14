import pytest

def calculer_racine(n) :
    if not isinstance (n,(float, int)):
        raise TypeError

    elif n < 0:
        raise ValueError

    else:
        return n ** 0.5


def test_TypeError():
    with pytest.raises (TypeError):
        calculer_racine("AZE")

def test_ValueError():
    with pytest.raises (ValueError):
        calculer_racine(-1)

def test_Normal():
    assert calculer_racine(9) == 3.0
    