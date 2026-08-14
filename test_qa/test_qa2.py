import pytest

def calculer_total_avec_remise(panier, remise):
    if not isinstance(panier, dict):
        raise TypeError("Le panier doit être un dictionnaire")
    return panier["total"] - remise

def test_calcul_remise_ok(panier_valide):
    resultat = calculer_total_avec_remise(panier_valide,10)
    assert resultat == pytest.approx (40.0)


def test_erreur_panier_invalide():
     with pytest.raises(TypeError, match="Le panier doit être un dictionnaire"):
         calculer_total_avec_remise("panier_cassé",10)
