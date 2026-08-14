# --- 1. Code applicatif à tester ---
def verifier_mot_de_passe(mdp: str) -> bool:
    if len(mdp) < 8:
        return False

    for char in mdp:
        if char.isdigit():
            return True

    return False


# --- 2. Campagne de tests (Jeux de données) ---
campagne_de_tests = [
    {"input": "Secret123", "attendu": True, "description": "Mot de passe valide"},
    {"input": "Pass123", "attendu": False, "description": "Trop court (7 chars)"},
    {"input": "MotDePasse", "attendu": False, "description": "Sans chiffre"},
    {"input": "", "attendu": False, "description": "Chaîne vide"},
]

# --- 3. Exécution automatique des tests ---
print("=== DÉBUT DU RUN DE TEST ===")

for test in campagne_de_tests:
    resultat = verifier_mot_de_passe(test["input"])

    # L'assertion vérifie que la valeur obtenue égale la valeur attendue
    assert resultat == test["attendu"], f"❌ ÉCHEC : {test['description']}"

    print(f"✅ PASS : {test['description']}")

print("=== TOUS LES TESTS SONT AU VERT ===")