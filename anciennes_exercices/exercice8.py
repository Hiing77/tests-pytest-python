def verifier_batterie(niveau):
    if niveau <= 15:
        return "CRITIQUE"
    elif niveau <= 50:
        return "FAIBLE"
    else:
        return "OK"

campagne_de_test = [
{"niveau": 10, "resultat": "CRITIQUE", "description": "Charger immédiatement"},
{"niveau": 50, "resultat": "FAIBLE", "description": "Batterie faible"},
{"niveau": 80, "resultat": "OK", "description": "Chargeur fonctionel"}
]

for test in campagne_de_test:
    resultat = verifier_batterie(test["niveau"])
   
    assert resultat == test["resultat"], f"❌ ÉCHEC : {test['description']}"
   
    print(f"✅ PASS : {test['description']}")
   
print("=== TOUS LES TESTS SONT AU VERT ===")