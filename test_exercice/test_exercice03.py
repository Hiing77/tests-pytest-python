def verifier_stock(quantite):
    if not isinstance(quantite, (int)):
            return "TYPE_INVALIDE"
    elif quantite < 0:
          return "NEGATIVE"
    elif quantite == 0:
        return "ZERO"
    elif quantite < 4:
          return "FAIBLE"
    else:
          return "SUFFISANTE"    

def test_TYPE_INVALIDE():
    assert verifier_stock("10") == "TYPE_INVALIDE"

def test_NEGATIVE():
    assert verifier_stock(-2) == "NEGATIVE"

def test_ZERO():
    assert verifier_stock(0) == "ZERO"

def test_FAIBLE():
    assert verifier_stock(3) == "FAIBLE"

def test_SUFFISANTE():
    assert verifier_stock(10) == "SUFFISANTE"