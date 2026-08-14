def verifier_paiement(solde, prix):
    if solde >= prix:
        return True

    else:
        return False
    
campagne_de_tests = [
{"solde": 100, "prix": 50, "attendu": True, "description": "Solde suffisant"},
{"solde": 50, "prix": 100, "attendu": False, "description": "Solde insuffisant"},
{"solde": 50, "prix": 50, "attendu": True, "description": "Solde suffisant"},
]

for test in campagne_de_tests:
    resultat = verifier_paiement(test["solde"],test["prix"])

    assert resultat == test["attendu"], f"❌ ÉCHEC : {test['description']}"
    
    print(f"✅ PASS : {test['description']}")
    
print("=== TOUS LES TESTS SONT AU VERT ===")

