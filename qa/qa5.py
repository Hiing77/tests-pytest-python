import pytest

def retirer_argent(compte, montant):
    if not isinstance (compte, (dict)):
        raise TypeError("Le compte doit être un dictionnaire")

    if not isinstance(montant, (int, float)):
        raise ValueError("La valeur est un chiffre ou nombre")

    elif compte["bloque"] == True:
        return "Compte bloqué"

    else:
        return compte["solde"] - montant

def test_retrait_reussi(compte_bancaire_actif):
    resultat = retirer_argent(compte_bancaire_actif, 100.0)
    assert resultat == pytest.approx(400.0)


def test_erreur_type_compte():
    with pytest.raises(TypeError, match="Le compte doit être un dictionnaire"):
        retirer_argent(12345,100.0)


