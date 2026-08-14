def verifier_acces(taille, age):
    if taille >= 140 and age >= 12:
        return True
    else:
        return False

campagne_de_tests = [
{"taille": 150, "age": 13, "resultat": True, "description": "Acces validé"},
{"taille": 145, "age": 11, "resultat": False, "description": "Acces non autorisé"},
{"taille": 139, "age": 14, "resultat": False, "description": "Acces non autorisé"},
{"taille": 135, "age": 10, "resultat": False, "description": "Acces non autorisé"}
]

for test in campagne_de_tests:
    resultat = verifier_acces(test["taille"],test["age"])
   
    assert resultat == test["resultat"], f"❌ ÉCHEC : {test['description']}"
   
    print(f"✅ PASS : {test['description']}")
   
print("=== TOUS LES TESTS SONT AU VERT ===")