import pytest

def calculer_prix_ttc(produit, taux_tva):
    if not isinstance (produit, (dict)):
        raise TypeError("Le produit doit être un dictionnaire")

    elif produit["en_stock"] == False:
        return 0.0

    else: 
        return produit["prix_ht"] * (1 + taux_tva)


def test_calcul_ttc_succes(produit_en_stock):
    resultat = calculer_prix_ttc(produit_en_stock, 0.20)
    assert resultat == pytest.approx(60.0) 

def test_erreur_type_produit():
    with pytest.raises(TypeError, match="Le produit doit être un dictionnaire"):
        calculer_prix_ttc("produit_invalide", 0.20)


def test_produit_hors_stock(produit_hors_stock):
    resultat = calculer_prix_ttc(produit_hors_stock, 0.20)
    assert resultat == 0.0
