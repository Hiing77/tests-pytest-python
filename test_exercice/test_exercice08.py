import pytest

def calculer_statut_membre(points):
    if not isinstance (points, (int)):
        return "TYPE_INVALIDE"
    
    elif points < 0:
        return "POINTS_INVALIDES"
    
    elif points >= 1000:
        return "PLATINE"

    elif points >= 500:
        return "OR"
    
    elif points >= 100:
        return "ARGENT"

    else:
        return"BRONZE"

@pytest.mark.parametrize (
"points, attendu",
        [
            ("AZER","TYPE_INVALIDE"),
            (-2, "POINTS_INVALIDES"),
            (1000, "PLATINE"),
            (500, "OR"),
            (100, "ARGENT"),
            (50, "BRONZE"),
        ]
)
def test_calculer_statut_membre(points, attendu):
    assert calculer_statut_membre(points) == attendu