
import builtins
from datetime import datetime
from src.main import App

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


class FakeDateTime:
    def __init__(self, fake_hour):
        self.fake_hour = fake_hour

    def now(self):
        class FakeNow:
            def __init__(self, hour):
                self.hour = hour
        return FakeNow(self.fake_hour)
