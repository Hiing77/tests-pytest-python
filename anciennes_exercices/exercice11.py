def verifier_inscription(age):
    if age < 0 or age > 100:
        return "AGE_INVALIDE"
    if age >= 16:
        return "AUTORISE"
    else:
        return "REFUSE"

campagne_de_tests = [
{"age": -1, "resultat": "AGE_INVALIDE", "description": "Age non conforme"},
{"age": 10, "resultat": "REFUSE", "description": "Age non autorisé"},
{"age": 99, "resultat": "AUTORISE", "description": "Age conforme"},
{"age": 16, "resultat": "AUTORISE", "description": "Age conforme"},
{"age": 101, "resultat": "AGE_INVALIDE", "description": "Age non conforme"}
]

for test in campagne_de_tests:
    resultat = verifier_inscription(test["age"])
   
    assert resultat == test["resultat"], f"❌ ÉCHEC : {test['description']}"
   
    print(f"✅ PASS : {test['description']}")
   
print("=== TOUS LES TESTS SONT AU VERT ===")