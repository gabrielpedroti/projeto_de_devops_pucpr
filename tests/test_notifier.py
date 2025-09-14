from src.notifier import send_notification

def test_notification_runs():
    # A função deve rodar e retornar True, mesmo fora do Windows
    assert send_notification() is True