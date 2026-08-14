def verifier_solde(solde) :
    if not isinstance(solde, (int,float)):
        return "TYPE_INVALIDE"
    elif solde < 0:
        return "SOLDE_NEGATIF"
    elif solde >= 1000 : 
        return "SOLDE_CONFORTABLE"
    else:
        return "SOLDE_POSITIF"

def test_TYPE_INVALIDE():
    assert verifier_solde("OK") == "TYPE_INVALIDE"

def test_SOLDE_NEGATIF():
    assert verifier_solde(-1) == "SOLDE_NEGATIF"

def test_SOLDE_CONFORTABLE():
    assert verifier_solde(1005) == "SOLDE_CONFORTABLE"

def test_SOLDE_POSITIF():
    assert verifier_solde(100) == "SOLDE_POSITIF"