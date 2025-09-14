import os
import sys

# garante que a raiz do repo esteja no PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.notifier import send_notification  # noqa: E402


def test_notification_runs():
    # A função deve rodar e retornar True, mesmo fora do Windows
    assert send_notification() is True
