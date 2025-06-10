
import builtins
from io import StringIO
from src.main import App

def test_mirror_inverts_word(monkeypatch, capsys):
    """L’application doit afficher le mot inversé."""
    # on simule l’entrée clavier de l’utilisateur
    monkeypatch.setattr(builtins, "input", lambda _: "Python")
    app = App()
    # exécution d’un seul tour de boucle
    app.once()
    captured = capsys.readouterr()
    assert "nohtyP" in captured.out
