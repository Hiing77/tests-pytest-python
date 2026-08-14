import pytest

def verifier_acces(role):
    if not isinstance(role, (str)):
        return "TYPE_INVALIDE"

    elif role == "admin":
        return "ACCES_TOTAL"

    elif role == "user":
        return "ACCES_RESTREINT"

    else:
        return "ACCES_REFUSE"

@pytest.mark.parametrize (
"role, attendu",
    [
        (12345, "TYPE_INVALIDE"),
        ("admin", "ACCES_TOTAL"),
        ("user", "ACCES_RESTREINT"),
        ("guest", "ACCES_REFUSE")
    ]

)


def test_verifier_acces(role, attendu):
    assert verifier_acces(role) == attendu