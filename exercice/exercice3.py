def verifier_vitesse(vitesse, limite):
    if vitesse <= limite:
        return True
    else:
        return False

campagne_de_tests = [
{"vitesse":50, "limite": 50, "resultat": True, "description": "Vitesse limite"},
{"vitesse":40, "limite": 50, "resultat": True, "description": "Vitesse normal"},
{"vitesse":55, "limite": 50, "resultat": False, "description": "Vitesse dépassé"}
]

for test in campagne_de_tests:
    resultat = verifier_vitesse(test["vitesse"],test["limite"])
   
    assert resultat == test["resultat"], f"❌ ÉCHEC : {test['description']}"
   
    print(f"✅ PASS : {test['description']}")
   
print("=== TOUS LES TESTS SONT AU VERT ===")