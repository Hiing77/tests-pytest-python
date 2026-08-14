import pytest

def calculer_reduction_fidelite(client, montant_achat):
    if not isinstance (client,(dict)):
        raise TypeError("Le client doit être un dictionnaire")

    if not isinstance (montant_achat, (int, float)):
        raise TypeError("Le montant doit être un nombre")

    elif montant_achat <= 0:
        raise ValueError("Le montant doit être strictement positif")

    elif client["statut"] == "GOLD":
        return montant_achat * 0.8
    
    elif client["statut"] == "SILVER":
        return montant_achat * 0.9
    
    else:
        return montant_achat * 1.0

@pytest.fixture
def client_gold():
    return {"nom": "Alex", "statut": "GOLD"}

@pytest.fixture
def client_silver():
    return {"nom": "Sam", "statut": "SILVER"}

def test_reduction_gold(client_gold):
    resultat = calculer_reduction_fidelite(client_gold, 100)
    assert resultat == pytest.approx (80.0)

def test_reduction_silver(client_silver):
    resultat = calculer_reduction_fidelite(client_silver, 100)
    assert resultat == pytest.approx (90.0)

def test_erreur_montant_negatif(client_gold):
    with pytest.raises(ValueError, match="Le montant doit être strictement positif"):
        calculer_reduction_fidelite(client_gold, -50)

def test_erreur_type_client():
    with pytest.raises(TypeError, match="Le client doit être un dictionnaire"):
        calculer_reduction_fidelite("chaine", 100)