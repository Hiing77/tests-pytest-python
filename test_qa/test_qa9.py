import pytest  
def calculer_prix_remise(prix, code_promo):

    if prix < 0:
        raise ValueError("Prix invalide")
    elif code_promo == "PROMO10":
        return prix * 0.90
    elif code_promo == "PROMO20":
        return prix * 0.80
    else:
        return prix


# 1. Test paramétré : lance 4 scénarios en une seule fonction
@pytest.mark.parametrize("prix, code_promo, attendu", [
    (100.0, "PROMO10", 90.0),  # Remise 10%
    (100.0, "PROMO20", 80.0),  # Remise 20%
    (100.0, "INVALIDE", 100.0), # Code inconnu -> Pas de réduction
    (100.0, None, 100.0),      # Pas de code -> Pas de réduction
])
def test_calculer_prix_remise_valide(prix, code_promo, attendu):
    assert calculer_prix_remise(prix, code_promo) == pytest.approx(attendu)


# 2. Test d'exception si le prix est négatif
def test_calculer_prix_remise_prix_negatif():
    with pytest.raises(ValueError, match="Prix invalide"):
        calculer_prix_remise(-10.0, "PROMO10")