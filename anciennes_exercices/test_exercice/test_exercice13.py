import pytest

def verifier_majorite(age):
    if age >= 18:
        return "Majeur"
    else:
        return "Mineur"


def test_majeur():
    assert verifier_majorite(20) == "Majeur"

def test_limite():
    assert verifier_majorite(18) == "Majeur"

def test_mineur():
    assert verifier_majorite(15) == "Mineur"