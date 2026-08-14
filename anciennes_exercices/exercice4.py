def verifier_temperature(temp_actuelle, temp_max):
    if temp_actuelle <= temp_max:
        return True
    else:
        return False

campagne_de_test = [
{"temp_actuelle": 27, "temp_max": 30, "resultat": True, "description": "Température parfaite pour le potager"},
{"temp_actuelle": 30, "temp_max": 30, "resultat": True, "description": "Température limite pour le potager"},
{"temp_actuelle": 33, "temp_max": 30, "resultat": False, "description": "Température trop forte pour le potager"},
]

for test in campagne_de_test:
    resultat = verifier_temperature(test["temp_actuelle"], test["temp_max"])

    assert resultat == test["resultat"], f"❌ ÉCHEC : {test['description']}"

    print(f"✅ PASS : {test['description']}")

print("=== TOUS LES TESTS SONT AU VERT ===")