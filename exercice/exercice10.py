def verifier_reduction(age, est_etudiant):
    if age < 26 or est_etudiant == True:
        return True
    else:
        return False

campagne_de_tests = [
{"age": 25, "est_etudiant": True, "resultat": True, "description": "Réduction accordée"},
{"age": 27, "est_etudiant": False, "resultat": False, "description": "Réduction non accordée"},
{"age": 26, "est_etudiant": True, "resultat": True, "description": "Réduction accordée"},
{"age": 29, "est_etudiant": False, "resultat": False, "description": "Réduction non accordée"}
]


for test in campagne_de_tests:
    resultat = verifier_reduction(test["age"],test["est_etudiant"])
   
    assert resultat == test["resultat"], f"❌ ÉCHEC : {test['description']}"
   
    print(f"✅ PASS : {test['description']}")
   
print("=== TOUS LES TESTS SONT AU VERT ===")