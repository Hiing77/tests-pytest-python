def verifier_age(age):
    if age >= 18:
        return True
    else:
        return False

cas_majeur = [
{"input": 20, "attendu": True, "description": "Age requis"},
{"input": 15, "attendu": False, "description": "Age non autorisé"},
{"input": 18, "attendu": True, "description": "Age autorisé limite"}
]

for test in cas_majeur:
    resultat = verifier_age(test["input"])

    assert resultat == test["attendu"], f"❌ ÉCHEC : {test['description']}"

    print(f"✅ PASS : {test['description']}")

print("=== TOUS LES TESTS SONT AU VERT ===")