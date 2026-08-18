import pytest

def verifier_acces_premium(utilisateur):
    if not isinstance (utilisateur, dict):
        raise TypeError("L'utilisateur doit être un dictionnaire")

    elif utilisateur["abonnement"] == "VIP":
        return "Accès Premium"

    else:
        return "Accès Standard"


def test_acces_vip_autorise(utilisateur_vip):
    resultat = verifier_acces_premium(utilisateur_vip)
    assert resultat == "Accès Premium"

def test_erreur_type_utilisateur():
    with pytest.raises(TypeError, match ="L'utilisateur doit être un dictionnaire"):
        verifier_acces_premium("pas_un_utilisateur")


def test_utilisateur_standard(utilisateur_standard):
    resultat = verifier_acces_premium(utilisateur_standard)
    assert resultat == "Accès Standard"