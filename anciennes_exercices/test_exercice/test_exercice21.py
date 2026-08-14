import pytest

def calculer_prix_solde(prix_initial, pourcentage_remise):
    if not isinstance (prix_initial, (int, float)):
        raise TypeError("Les arguments doivent être des nombres")

    if not isinstance (pourcentage_remise, (int, float)):
        raise TypeError("Les arguments doivent être des nombres")

    elif prix_initial <= 0:
        raise ValueError("Le prix doit être strictement positif")

    elif pourcentage_remise < 0 or pourcentage_remise > 100:
        raise ValueError("La remise doit être entre 0 et 100")

    else:
        return prix_initial - (prix_initial * pourcentage_remise / 100)

@pytest.mark.parametrize("prix_initial, pourcentage_remise, resultat_attendu",[
    (100, 20, 80),   # Cas 1 : 100€ - 20% = 80€
    (50, 10, 45),    # Cas 2 : 50€ - 10% = 45€
    (200, 50, 100)   # Cas 3 : 200€ - 50% = 100€)
])

def test_calculer_prix_solde_cas_normaux(prix_initial, pourcentage_remise, resultat_attendu):
    assert calculer_prix_solde(prix_initial,pourcentage_remise) == resultat_attendu

