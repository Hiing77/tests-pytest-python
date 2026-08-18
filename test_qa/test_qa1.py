import pytest

def verifier_acces_admin(compte):
    if not isinstance (compte,(dict)):
        raise TypeError("Le compte doit être un dictionnaire")

    
    if compte["role"] == "ADMIN" and compte["actif"] == True:
        return "Accès autorisé"

    else:
        return "Accès refusé"

def test_acces_admin_autorise(profil_admin):
        resultat = verifier_acces_admin(profil_admin)
        assert resultat == "Accès autorisé"

def test_erreur_type_compte():
    with pytest.raises(TypeError, match="Le compte doit être un dictionnaire"):
        verifier_acces_admin("pas_un_dict")

def test_acces_admin_refuse(compte_utilisateur_standard):
    resultat = verifier_acces_admin(compte_utilisateur_standard)
    assert resultat == "Accès refusé"