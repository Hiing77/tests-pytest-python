def verifier_virement(montant):
    if montant <= 0 or montant > 5000:
        return "MONTANT_INVALIDE"

    if montant >= 1000:
        return "VALIDATION_REQUISE"

    else:
        return "VALIDE"

campagne_de_tests = [
{"montant": -1, "resultat": "MONTANT_INVALIDE", "description": "Montant non conforme"},
{"montant": 1001, "resultat": "VALIDATION_REQUISE", "description": "Montant à confirmer"},
{"montant": 100, "resultat": "VALIDE", "description": "Montant validé"},
]

for test in campagne_de_tests:
    resultat = verifier_virement(test["montant"])
   
    assert resultat == test["resultat"], f"❌ ÉCHEC : {test['description']}"
   
    print(f"✅ PASS : {test['description']}")
   
print("=== TOUS LES TESTS SONT AU VERT ===")