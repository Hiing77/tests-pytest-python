import pytest

def est_nombre_pair(n):
    if n % 2:
        return False

    else:
        return True


def test_pair():
    assert est_nombre_pair(4) == True
    
def test_impair():
    assert est_nombre_pair(7) == False

def test_zero():
    assert est_nombre_pair(0) == True