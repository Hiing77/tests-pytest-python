from tests_python import verifier_mot_de_passe


def test_mot_de_passe_valide():
    assert verifier_mot_de_passe("Secret123") == True


def test_mot_de_passe_trop_court():
    assert verifier_mot_de_passe("Pass123") == False


def test_mot_de_passe_sans_chiffre():
    assert verifier_mot_de_passe("MotDePasse") == False