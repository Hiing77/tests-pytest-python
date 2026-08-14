def verifier_note(note, note_passage):
    if note >= note_passage:
        return True
    else:
        return False

campagne_de_test = [
{"note": 11, "note_passage": 10, "resultat": True, "description": "Examen réussi"},
{"note": 9, "note_passage": 10, "resultat": False, "description": "Examen à repasser"},
{"note": 10, "note_passage": 10, "resultat": True, "description": "Examen réussi(limite)"}
]

for test in campagne_de_test:
    resultat = verifier_note(test["note"], test["note_passage"])

    assert resultat == test["resultat"], f"❌ ÉCHEC : {test['description']}"

    print(f"✅ PASS : {test['description']}")

print("=== TOUS LES TESTS SONT AU VERT ===")