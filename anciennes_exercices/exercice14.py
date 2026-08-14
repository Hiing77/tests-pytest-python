def calculer_tarif_cinema(age) :
    if age < 12:
        return "ENFANT"
    if age >= 60:
        return "SENIOR"
    else:
        return "PLEIN_TARIF"

campagne_de_tests = [
{"age": 11,"resultat":"ENFANT", "description":"Tarif enfant"},
{"age": 60,"resultat":"SENIOR", "description":"Tarif senior"},
{"age": 61,"resultat":"SENIOR", "description":"Tarif senior"},
{"age": 13,"resultat":"PLEIN_TARIF", "description":"Plein tarif"},
{"age": 12,"resultat":"PLEIN_TARIF", "description":"Plein tarif"}
]


for test in campagne_de_tests:
    resultat = calculer_tarif_cinema(test["age"])
   
    assert resultat == test["resultat"], f"❌ ÉCHEC : {test['description']}"
   
    print(f"✅ PASS : {test['description']}")
   
print("=== TOUS LES TESTS SONT AU VERT ===")