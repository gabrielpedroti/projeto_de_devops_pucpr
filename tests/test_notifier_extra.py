import sys
import types
import platform


# Importa a função a ser testada
from src.notifier import send_notification


def test_non_windows_returns_true(capsys, monkeypatch):
    """Quando não for Windows, deve apenas simular e retornar True."""
    monkeypatch.setattr(platform, "system", lambda: "Linux")
    assert send_notification() is True
    captured = capsys.readouterr()
    assert "Simulação: Verificar mensagens" in captured.out


def test_non_windows_is_idempotent(monkeypatch):
    """Chamar várias vezes fora do Windows não deve quebrar."""
    monkeypatch.setattr(platform, "system", lambda: "Darwin")
    for _ in range(3):
        assert send_notification() is True


def test_windows_path_returns_true(monkeypatch):
    """No caminho Windows, a função também deve retornar True."""
    # Finge que estamos no Windows
    monkeypatch.setattr(platform, "system", lambda: "Windows")

    # Cria um módulo fake 'winotify' com uma classe Notification mínima
    fake_module = types.ModuleType("winotify")

    class FakeNotification:
        def __init__(self, app_id, title, msg, duration):
            self.app_id = app_id
            self.title = title
            self.msg = msg
            self.duration = duration
            self._shown = False

        def show(self):
            self._shown = True

    fake_module.Notification = FakeNotification
    monkeypatch.setitem(sys.modules, "winotify", fake_module)

    assert send_notification() is True  # não deve levantar exceção


def test_windows_notification_parameters(monkeypatch):
    """Garante que os parâmetros passados à Notification são os esperados."""
    monkeypatch.setattr(platform, "system", lambda: "Windows")

    # Módulo winotify fake com verificação dos argumentos
    captured = {}

    class FakeNotification:
        def __init__(self, app_id, title, msg, duration):
            captured["app_id"] = app_id
            captured["title"] = title
            captured["msg"] = msg
            captured["duration"] = duration

        def show(self):
            captured["shown"] = True

    fake_module = types.ModuleType("winotify")
    fake_module.Notification = FakeNotification
    monkeypatch.setitem(sys.modules, "winotify", fake_module)

    assert send_notification() is True
    assert captured["app_id"] == "Notificador DevOps"
    assert captured["title"] == "Lembrete de Tarefas"
    assert "WhatsApp" in captured["msg"]
    assert captured["duration"] in {"short", "long"}
    assert captured.get("shown") is True


def test_docstring_exists():
    """Só pra garantir documentação mínima da função pública."""
    assert isinstance(send_notification.__doc__, str)
    assert "notificação" in send_notification.__doc__.lower()
