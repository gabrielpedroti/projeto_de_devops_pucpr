import platform


def send_notification():
    """Envia uma notificação no Windows 10/11.
    Em outros SOs, apenas simula (print) para o CI não quebrar.
    """
    if platform.system() != "Windows":
        print("Simulação: Verificar mensagens no WhatsApp e ordem de serviços")
        return True

    # Importa somente no Windows para evitar erros no CI (Linux)
    from winotify import Notification

    notificacao = Notification(
        app_id="Notificador DevOps",
        title="Lembrete de Tarefas",
        msg="Verificar mensagens no WhatsApp e ordem de serviços",
        duration="short",
    )
    notificacao.show()
    return True


if __name__ == "__main__":
    send_notification()
