import pytest

def calculer_frais_livraison(poids, distance):
    if not isinstance (poids, (int,float)):
        raise TypeError("Les arguments doivent être des nombres")

    if not isinstance (distance, (int,float)):
        raise TypeError("Les arguments doivent être des nombres")

    elif poids <= 0 or distance <= 0:
        raise ValueError("Le poids et la distance doivent être strictement positifs")
    
    else:
        return (poids * 2) + (distance * 0.5)


@pytest.mark.parametrize("poids, distance, resultat_attendu",[
    (5, 10, 15.0),
    (4, 20, 18.0),
    (406, 2, 813.0)
    ])

def test_calculer_frais_cas_normaux(poids, distance, resultat_attendu):
    assert calculer_frais_livraison(poids, distance) == resultat_attendu

def test_erreur_type():
    with pytest.raises(TypeError, match="Les arguments doivent être des nombres"):
        calculer_frais_livraison("cinq", 10)

def test_erreur_valeur():
    with pytest.raises(ValueError, match="Le poids et la distance doivent être strictement positifs"):
        calculer_frais_livraison(0, 10)