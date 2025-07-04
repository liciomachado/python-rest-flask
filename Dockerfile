FROM python:3.10-slim

WORKDIR /app

COPY . /app

# Instala dependências
RUN pip install --upgrade pip && \
    pip install uvicorn gunicorn && \
    pip install -r requirements.txt

# Define ENV default
ENV ENV=production

# Usa o ENV correto (ou sobrescreve com docker-compose)
CMD ["python", "run.py"]