def calculer_remise(prix):
    if not isinstance(prix, (int, float)):
        return "TYPE_INVALIDE"
    
    elif prix <= 0:
        return "PRIX_INVALIDE"

    elif prix >= 100:
        return "REMISE_ACCORDEE"

    else:
        return "PAS_DE_REMISE"

campagne_de_tests = [
{"prix": "100", "resultat":"TYPE_INVALIDE", "description": "Saisie invalide"},
{"prix": "OK", "resultat":"TYPE_INVALIDE", "description": "Saisie invalide"},
{"prix": 0, "resultat":"PRIX_INVALIDE", "description": "Erreur prix"},
{"prix": 100, "resultat":"REMISE_ACCORDEE", "description": "Remise validé"},
{"prix": 90, "resultat":"PAS_DE_REMISE", "description": "Aucune remise"}
]

for test in campagne_de_tests:
    resultat = calculer_remise(test["prix"])
   
    assert resultat == test["resultat"], f"❌ ÉCHEC : {test['description']}"
   
    print(f"✅ PASS : {test['description']}")
   