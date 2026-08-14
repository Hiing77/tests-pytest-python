def verifier_age(age) :
    if not isinstance(age, (int)):
        return "TYPE_INVALIDE"
    elif age < 0 or age > 120:
        return "AGE_INVALIDE"
    elif age < 12:
        return "TARIF_ENFANT"
    elif age < 18:
        return "TARIF_MINEUR"
    else:
        return "TARIF_ADULTE"


def test_TYPE_INVALIDE():
    assert verifier_age("ok") == "TYPE_INVALIDE"

def test_AGE_INVALIDE():
    assert verifier_age(125) == "AGE_INVALIDE"

def test_TARIF_ENFANT():
    assert verifier_age(11) == "TARIF_ENFANT"

def test_TARIF_MINEUR():
    assert verifier_age(17) == "TARIF_MINEUR"

def test_TARIF_ADULTE():
    assert verifier_age(34) == "TARIF_ADULTE"
