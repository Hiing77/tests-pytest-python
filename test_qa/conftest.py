import pytest

@pytest.fixture
def profil_admin():
    return {"utilisateur": "Miya", "role": "ADMIN", "actif": True}

@pytest.fixture
def panier_valide():
    return {"articles": ["Livre", "Stylo"], "total": 50.0}

@pytest.fixture
def commande_express():
    return {"type": "EXPRESS", "poids_kg": 2.5, "montant_base": 15.0}

@pytest.fixture
def utilisateur_vip():
    return {"nom": "Alex", "abonnement": "VIP", "solde": 100.0}

@pytest.fixture
def compte_bancaire_actif():
    return {"iban": "FR7612345", "solde": 500.0, "bloque": False}

@pytest.fixture
def client_fidele():
    return {"nom": "Julie", "statut": "GOLD", "montant_achats": 150.0}

@pytest.fixture
def produit_en_stock():
    return {"nom": "Clavier", "prix_ht": 50.0, "en_stock": True}