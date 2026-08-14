import pytest

def calculer_frais_livraison(montant):
    if not isinstance(montant,(float, int)):
        return "TYPE_INVALIDE"

    elif montant < 0:
        return "MONTANT_INVALIDE"

    elif montant >= 100:
        return "GRATUIT"

    elif montant >= 50:
        return "FRAIS_REDUITS"

    else:
        return "FRAIS_STANDARDS"

@pytest.mark.parametrize (
"montant, attendu",
    [
        ("ALEX", "TYPE_INVALIDE"),
        (-1, "MONTANT_INVALIDE"),
        (100, "GRATUIT"),
        (50, "FRAIS_REDUITS"),
        (10, "FRAIS_STANDARDS")
    ]

)

def test_calculer_frais_livraison(montant, attendu):
    assert calculer_frais_livraison(montant) == attendu