import pytest

def calculer_prix_ttc(prix_ht, taux_tva):
    if not isinstance (prix_ht,(int,float)):
        raise TypeError("Les arguments doivent être des nombres")
    
    if not isinstance (taux_tva,(int,float)):
        raise TypeError("Les arguments doivent être des nombres")

    elif prix_ht <= 0 or taux_tva < 0:
        raise ValueError("Le prix HT doit être positif et le taux de TVA non négatif")

    else:
        return prix_ht * (1 + taux_tva / 100)

@pytest.mark.parametrize("prix_ht, taux_tva, resultat_attendu",[
    (100, 20, 120.0),
    (50, 10, 55.0),
    (200, 0, 200.0)
])

def test_calcul_ttc_cas_normaux(prix_ht, taux_tva, resultat_attendu):
    assert calculer_prix_ttc(prix_ht, taux_tva) == pytest.approx(resultat_attendu)

def test_erreur_type():
    with pytest.raises(TypeError, match="Les arguments doivent être des nombres"):
        calculer_prix_ttc("AZE", "ok")

def test_erreur_valeur():
    with pytest.raises(ValueError, match="Le prix HT doit être positif et le taux de TVA non négatif"):
        calculer_prix_ttc(0, -1)