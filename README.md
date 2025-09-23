## **Sistema de Notificações Windows (DevOps)**

Projeto desenvolvido na disciplina de **DevOps** na PUC-PR, com o objetivo de aplicar conceitos fundamentais de DevOps, como **CI/CD**, uso de **Docker**, práticas com **Git/GitHub** e automação de fluxos com **GitHub Actions**.

Para colocar tudo isso em prática, foi criado um projeto em **Python** que exibe notificações no **Windows 10/11**.  
A mensagem usada como exemplo foi:

> *"Verificar mensagens no WhatsApp e ordem de serviços"*

No Windows, a notificação aparece normalmente na área de trabalho.  
Em outros sistemas (Linux, macOS ou no próprio GitHub Actions), o comportamento é simulado via `print`, garantindo que o pipeline funcione em qualquer ambiente.

---

### **Etapas do Projeto**
- **Atividade Formativa - Semana 2:** configuração do fluxo de **CI**, rodando testes automatizados (`pytest`) e checagem de estilo (`flake8`).  
- **Atividade Formativa - Semana 3:** implementação do fluxo de **CD**, empacotando o projeto em um `.zip` publicado como artifact.  
- **Somativa 1 - Semana 4:** criação de um **Dockerfile** e workflow para build e execução em container, validando a aplicação diretamente no GitHub Actions.  
- **Atividade Formativa - Semana 6:** configuração de workflow de **alertas**, que gera notificações automáticas em *Pull Requests* ou abre issues em caso de falhas no CI.  
- **Somativa 2 - Semana 7:** adição de uma suíte de **testes unitários extras**, cobrindo diferentes cenários da aplicação, e validação desses testes dentro de uma **PR** com todos os workflows (CI, CD e Docker) executando com sucesso.

---

### **Status**
O projeto foi finalizado até a **Somativa 2 (Semana 7)**, servindo como prática completa dos principais conceitos de DevOps:  
- **Integração Contínua (CI)**  
- **Entrega Contínua (CD)**  
- **Containerização com Docker**  
- **Automação de fluxos no GitHub Actions**  
- **Alertas automáticos**  
- **Testes unitários em PR**

Este repositório se mantém como base prática para consultas futuras e referência no aprendizado contínuo de DevOps.
