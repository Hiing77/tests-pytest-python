def evaluer_note(note) :
    if note < 0 or note > 20:
        return "NOTE_INVALIDE"
    elif note < 10:
        return "NON_VALIDE"
    else:
        return "VALIDE"

campagne_de_tests = [
{"note": -1, "resultat": "NOTE_INVALIDE", "description": "Erreur"},
{"note": 21, "resultat": "NOTE_INVALIDE", "description": "Erreur"},
{"note": 9, "resultat": "NON_VALIDE", "description": "Insuffisant"},
{"note": 10, "resultat": "VALIDE", "description": "Valide"},
{"note": 13, "resultat": "VALIDE", "description": "Valide"}
]

for test in campagne_de_tests:
    resultat = evaluer_note(test["note"])
   
    assert resultat == test["resultat"], f"❌ ÉCHEC : {test['description']}"
   
    print(f"✅ PASS : {test['description']}")
   
print("=== TOUS LES TESTS SONT AU VERT ===")