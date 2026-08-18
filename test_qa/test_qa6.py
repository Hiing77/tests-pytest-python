import pytest

def calculer_points_bonus(client, multiplicateur):
    if not isinstance (client,(dict)):
        raise TypeError("Le client doit être un dictionnaire")

    elif client["statut"] == "GOLD":
        return client["montant_achats"] * multiplicateur * 2

    else:
        return client["montant_achats"] * multiplicateur

def test_points_client_gold(client_fidele):
    resultat = calculer_points_bonus(client_fidele, 2 )
    assert resultat == pytest.approx(600.0)

def test_erreur_type_client():
    with pytest.raises(TypeError, match ="Le client doit être un dictionnaire"):
            calculer_points_bonus("client_invalide", 2)

def test_frais_livraison_standard(client_standard):
    resultat = calculer_points_bonus(client_standard, 2)
    assert resultat == pytest.approx(100.0 * 2)

