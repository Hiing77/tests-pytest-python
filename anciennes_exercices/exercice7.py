def verifier_alerte(temp):
    if temp > 80:
        return "DANGER"
    elif temp >= 50:
        return "ATTENTION"
    else:
        return "OK"

campagne_de_test = [
{"temp": 50, "resultat": "ATTENTION", "description": "Attention température du serveur limite"},
{"temp": 81, "resultat": "DANGER", "description": "Danger serveur surchauffe"},
{"temp": 40, "resultat": "OK", "description": "Serveur normal"}
]

for test in campagne_de_test:
    resultat = verifier_alerte(test["temp"])

    assert resultat == test["resultat"], f"❌ ÉCHEC : {test['description']}"

    print(f"✅ PASS : {test['description']}")

print("=== TOUS LES TESTS SONT AU VERT ===")