import pytest

def calculer_frais_livraison(montant_panier, est_membre_vip):
    if montant_panier < 0:
        raise ValueError("Le montant du panier ne peut pas être négatif")

    if est_membre_vip or montant_panier >= 100:
        return 0.0

    return 8.50

def test_livraison_payante(commande_standard):
    resultat = calculer_frais_livraison(
        commande_standard["montant"], commande_standard["is_vip"]
    )
    assert resultat == pytest.approx(8.50)


# 2. Test livraison gratuite panier >= 100€ (non-VIP)
def test_livraison_gratuite_panier_100():
    resultat = calculer_frais_livraison(100.0, False)
    assert resultat == 0.0


# 3. Test livraison gratuite client VIP (petit panier)
def test_livraison_gratuite_vip():
    resultat = calculer_frais_livraison(20.0, True)
    assert resultat == 0.0


# 4. Test exception si montant négatif
def test_livraison_montant_negatif():
    with pytest.raises(
        ValueError, match="Le montant du panier ne peut pas être négatif"
    ):
        calculer_frais_livraison(-10.0, False)