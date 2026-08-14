import pytest

def evaluer_note(note) :
    if not isinstance(note, (int,float)):
        return "TYPE_INVALIDE"
    elif note < 0 or note > 20:
        return "NOTE_INVALIDE"

    elif note >= 10:
        return "ADMIS"

    else:
        return "AJOURNE"

@pytest.mark.parametrize(
"note, attendu",
    [
        ("ok", "TYPE_INVALIDE"),
        (-2, "NOTE_INVALIDE"),
        (10, "ADMIS"),
        (5, "AJOURNE")
    ],
)

def test_evaluer_note(note, attendu):
    assert evaluer_note(note) == attendu