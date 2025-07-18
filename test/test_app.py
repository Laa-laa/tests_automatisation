
import builtins
import pytest
from datetime import datetime
from src.main import App
from src.ohce import OHCE
from test_ohce_builder import OHCEBuilder
from src.langues import FR, EN

@pytest.fixture               # ← décorateur obligatoire
def ohce():
    """Instancie OHCE pour chaque test qui en a besoin."""
    return OHCE()


def test_non_palindrome(ohce):
    attendu = "bonjour\ntahc\nau revoir"
    assert ohce.Palindrome("chat") == attendu


def test_palindrome(ohce):
    attendu = "bonjour\nkayak\nBien dit!\nau revoir"
    assert ohce.Palindrome("kayak") == attendu


def test_mot_mirroir(monkeypatch, capsys):
    """L’application doit afficher le mot inversé."""
    monkeypatch.setattr(builtins, "input", lambda _: "Python")
    app = App()
    app.once()
    captured = capsys.readouterr()
    assert "nohtyP" in captured.out

def test_bonjour(monkeypatch):
    """Doit dire 'Bonjour' entre 5h et 17h."""
    monkeypatch.setattr("src.main.datetime", FakeDateTime(8))
    app = App()
    assert app.saluer() == "Bonjour"

def test_bonsoir(monkeypatch):
    """Doit dire 'Bonsoir' entre 18h et 4h."""
    monkeypatch.setattr("src.main.datetime", FakeDateTime(19))
    app = App()
    assert app.saluer() == "Bonsoir"

def test_cycle_complet(monkeypatch, capsys):
    inputs = iter(["kayak"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    app = App()
    app.once()
    captured = capsys.readouterr()
    assert "kayak" in captured.out
    assert "Bien dit!" in captured.out
    assert "au revoir" in captured.out

def test_palindrome_en_francais():
    ohce = OHCEBuilder().parlant(FR).build()
    result = ohce.Palindrome("kayak")
    assert result == "bonjour\nkayak\nBien dit!\nau revoir"


def test_palindrome_en_anglais():
    ohce = OHCEBuilder().parlant(EN).build()
    result = ohce.Palindrome("madam")
    assert result == "hello\nmadam\nWell said!\ngoodbye"


def test_non_palindrome_en_fr():
    ohce = OHCEBuilder().parlant(FR).build()
    result = ohce.Palindrome("chat")
    assert result == "bonjour\ntahc\nau revoir"


def test_salutations_en_anglais():
    ohce = OHCEBuilder().parlant(EN).build()
    result = ohce.Palindrome("cat")
    assert result.startswith("hello")
    assert result.endswith("goodbye")


class FakeDateTime:
    def __init__(self, fake_hour):
        self.fake_hour = fake_hour

    def now(self):
        class FakeNow:
            def __init__(self, hour):
                self.hour = hour
        return FakeNow(self.fake_hour)
