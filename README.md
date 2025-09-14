# Projeto de Notificações Windows (Faculdade - DevOps)

Este projeto em Python implementa um sistema simples de **notificações no Windows 10/11**,
servindo como base para as atividades das semanas 2, 3 e 4 da disciplina de DevOps.

## Objetivo
- Demonstrar o uso de **CI/CD (Semana 2)** no GitHub Actions.
- Empacotar o projeto em **Docker (Semana 3)**.
- Consolidar o aprendizado em uma **atividade somativa (Semana 4)**.

## Como funciona
A função principal envia uma notificação com a mensagem:

> "Verificar mensagens no WhatsApp e ordem de serviços"

## Como rodar localmente (Windows)
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/notifier.py
```

## Testes
Os testes usam `pytest` para validar que a função principal roda sem erro.

```bash
pytest -q
```

## Estrutura
```
.
├── .github/workflows/ci.yml
├── requirements.txt
├── src/notifier.py
├── tests/test_notifier.py
└── README.md
```

## Fluxo de CI/CD (Semana 2)
- CI roda em **cada push e PR** para a branch `main`.
- Pipeline executa:
  - Instalação das dependências
  - Lint (`flake8`)
  - Testes (`pytest`)

## Próximos passos
- Semana 3: adicionar Dockerfile e rodar o app em container.
- Semana 4: consolidar tudo na somativa.
