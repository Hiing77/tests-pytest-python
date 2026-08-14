import pytest

def calculer_inverse(n):
    if not isinstance (n,(int,float)):
        raise TypeError

    elif n == 0 :
        raise ValueError

    else:
        return 1 / n

def test_erreur_type():
    with pytest.raises(TypeError):
        calculer_inverse("OK")

def test_erreur_valeur():
    with pytest.raises(ValueError):
        calculer_inverse(0)

def test_cas_normal():
        assert calculer_inverse(2) == 0.5
        