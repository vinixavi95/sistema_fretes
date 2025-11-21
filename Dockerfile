# Usando Python 3.12 slim
FROM python:3.12-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar requirements e instalar dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o projeto
COPY . /app/

# Adicionar src ao PYTHONPATH para não mexer nos imports
ENV PYTHONPATH=/app/src

# Expor porta do FastAPI
EXPOSE 8000

# Comando padrão
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]