import pytest

def calculer_frais_livraison(commande):
    if not isinstance (commande, (dict)):
        raise TypeError("La commande doit être un dictionnaire")

    elif commande["type"] == "EXPRESS":
        return commande["montant_base"] + 10.0

    else:
        return commande["montant_base"]

def test_frais_livraison_express(commande_express):
    resultat = calculer_frais_livraison(commande_express)
    assert resultat == pytest.approx (25.0)
    
def test_erreur_commande_invalide():
    with pytest.raises(TypeError, match="La commande doit être un dictionnaire"):
         calculer_frais_livraison("livraison_status")

