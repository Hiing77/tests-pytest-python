def calculer_frais_livraison(poids) :
    if poids <= 0 or poids > 30:
        return "POIDS_INVALIDE"

    if poids <= 5:
        return "GRATUIT"

    else: 
        return "STANDARD"

campagne_de_tests = [
{"poids":-2, "resultat": "POIDS_INVALIDE", "description": "Erreur"},
{"poids":5, "resultat": "GRATUIT", "description": "Livraison gratuite"},
{"poids":31, "resultat": "POIDS_INVALIDE", "description": "Erreur"},
{"poids":12, "resultat": "STANDARD", "description": "Livraison payante"},
{"poids":0, "resultat": "POIDS_INVALIDE", "description": "Erreur"}
]

for test in campagne_de_tests:
    resultat = calculer_frais_livraison(test["poids"])
   
    assert resultat == test["resultat"], f"❌ ÉCHEC : {test['description']}"
   
    print(f"✅ PASS : {test['description']}")
   
print("=== TOUS LES TESTS SONT AU VERT ===")