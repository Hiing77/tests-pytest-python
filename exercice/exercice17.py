def verifier_vitesse(vitesse):
    if not isinstance(vitesse, (int,float)):
        return "TYPE_INVALIDE"
    elif vitesse < 0 or vitesse > 300:
        return "VITESSE_INVALIDE"
    elif vitesse > 130:
        return "EXCES_DE_VITESSE"
    else:
        return "CONFORME"

campagne_de_tests = [
{"vitesse": "OK", "resultat": "TYPE_INVALIDE", "description": "Erreur"},
{"vitesse": "90", "resultat": "TYPE_INVALIDE", "description": "Erreur"},
{"vitesse": -30, "resultat": "VITESSE_INVALIDE", "description": "Vitesse invalide"},
{"vitesse": 301, "resultat": "VITESSE_INVALIDE", "description": "Vitesse invalide"},
{"vitesse": 300, "resultat": "EXCES_DE_VITESSE", "description": "Exces de vitesse"},
{"vitesse": 300, "resultat": "EXCES_DE_VITESSE", "description": "Exces de vitesse"},
{"vitesse": 150, "resultat": "EXCES_DE_VITESSE", "description": "Exces de vitesse"},
{"vitesse": 50, "resultat": "CONFORME", "description": "Vitesse autorisé"},
]


for test in campagne_de_tests:
    resultat = verifier_vitesse(test["vitesse"])
   
    assert resultat == test["resultat"], f"❌ ÉCHEC : {test['description']}"
   
    print(f"✅ PASS : {test['description']}")
   