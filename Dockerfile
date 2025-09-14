# Imagem base pequena e estável
FROM python:3.11-slim

# Não escrever pyc e buffer para logs legíveis
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Copia dependências primeiro (melhor cache)
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

# Copia o código
COPY src /app/src
COPY README.md /app/README.md

# Ponto de entrada: roda a app
CMD ["python", "src/notifier.py"]
