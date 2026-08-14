def verifier_poids(poids_bagage, poids_max):
    if poids_bagage <= poids_max:
        return True
    else:
        return False

campagne_de_tests = [
{"poids_bagage": 23, "poids_max": 23, "resultat": True, "description":"Poids limite"},
{"poids_bagage": 27, "poids_max": 23, "resultat": False, "description":"Poids dépassé"},
{"poids_bagage": 20, "poids_max": 23, "resultat": True, "description":"Poids confirmé"}
]

for test in campagne_de_tests:
    resultat = verifier_poids(test["poids_bagage"],test["poids_max"])

    assert resultat == test["resultat"], f"❌ ÉCHEC : {test['description']}"
    
    print(f"✅ PASS : {test['description']}")
    
print("=== TOUS LES TESTS SONT AU VERT ===")
