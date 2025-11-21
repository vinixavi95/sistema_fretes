#📦 Sistema de Fretes — Backend (FastAPI)

Este projeto implementa um servidor backend completo para um sistema de fretes, permitindo que usuários:

Se autentiquem

Solicitem fretes

Realizem pagamentos

Consultem históricos

Acessem relatórios conforme seu cargo (gerente, entregador ou usuário comum)

A API foi construída com FastAPI, executada via Uvicorn, utiliza PostgreSQL como banco de dados e integra com APIs externas:

BrasilAPI — consulta de CEP e coordenadas

Project OSRM — cálculo de distância geográfica

#🚀 Funcionalidades
👤 Usuário

Cadastro

Login (gera token JWT)

Atualização de dados

Solicitação de frete

Pagamento de frete

Histórico de fretes

🧑‍💼 Funcionário

Cadastro como funcionário (após criar conta)

Consulta de fretes por entregadores

Relatórios de fretes por gerentes

Registro de ponto (entrada/saída)

🗄️ Arquitetura da API

O projeto segue uma separação clara de responsabilidades:

route → controller → service → repository


route: recebe requisições HTTP

controller: valida e orquestra chamadas

service: regras de negócio

repository: acesso ao banco de dados

🛠️ Tecnologias Utilizadas

Python 3.13

FastAPI

Uvicorn

PostgreSQL

psycopg2

python-jose (JWT)

APIs externas: BrasilAPI, OSRM

#▶️ Como Executar o Projeto
1. Clonar o repositório
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

2. Instalação de dependências (opcional, sem Docker)

Se quiser rodar localmente sem Docker:

# Criar e ativar ambiente virtual
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

# Atualizar pip e instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

3. Rodar o projeto

Com Docker (recomendado):

docker compose up --build


A imagem já inclui o PostgreSQL e o script de inicialização do banco.

Sem Docker:

uvicorn main:app --reload


O servidor ficará disponível em http://127.0.0.1:8000
.

#4. Documentação automática

O FastAPI fornece interface Swagger interativa:

http://127.0.0.1:8000/docs

#🗄️ Banco de Dados

Com Docker: já vem configurado e inicializado

Sem Docker: configure um PostgreSQL local e execute o script fretes.sql

#🔐 Fluxo de Autenticação

Cadastro → cria o usuário

Login → gera o token JWT

Usar o token no header:

Authorization: Bearer <seu_token>

🔑 Endpoints
👤 Cadastro de Usuário

POST /usuario/cadastro

{
  "nome": "string",
  "email": "string",
  "senha": "string",
  "telefone": 11999999999,
  "eh_funcionario": false
}

🔑 Login

POST /usuario/login

{
  "email": "string",
  "senha": "string"
}


Retorno:

{
  "access_token": "string",
  "token_type": "bearer"
}

🧑‍💼 Cadastro de Funcionário

POST /usuario/funcionario (token necessário)

{
  "usuario_id": 1,
  "cargo": "gerente",
  "numero_registro": 12345
}

✏️ Atualizar Usuário

PUT /usuario/atualizar

{
  "nome": "string",
  "email": "user@example.com",
  "senha": "string"
}

🚚 Fretes
📦 Solicitação de Frete

POST /frete/solicitacao (token necessário)

{
  "peso": 3.2,
  "opcao": 1,
  "cep_origem": "01001000",
  "cep_destino": "20040030"
}


Retorno:

{
  "frete_id": 1,
  "valor": 45.90,
  "tipo": "Expresso",
  "status": "calculado"
}


⚠️ Observação: A BrasilAPI pode apresentar instabilidades na devolução de coordenadas, o que impede o cálculo do frete.

💳 Pagamento do Frete

POST /frete/pagamento

{
  "frete_id": 1,
  "meio_pagamento": "pix"
}


Retorno:

{
  "frete_id": 1,
  "status": "pago",
  "meio_pagamento": "pix"
}

📜 Histórico de Fretes

GET /frete/historico (apenas gerentes)

Retorno:

{
  "fretes": [
    "..."
  ]
}

🔍 Consulta de Frete (Entregador)

GET /frete/consulta?frete_id=1 (apenas entregador)

Retorno:

{
  "cep_origem": "string",
  "cep_destino": "string",
  "nome_remetente": "string",
  "telefone_remetente": "string"
}

📊 Relatórios
📅 Fretes do Dia

GET /relatorio/fretes-dia?data_consulta=YYYY-MM-DD (opcional)

[
  {
    "frete_id": 1,
    "status": "pago",
    "valor": 40,
    "meio_pagamento": "pix",
    "mensagem": "OK"
  }
]

⏱️ Registro de Ponto

POST /relatorio/ponto

{
  "tipo": "entrada"
}


Retorno:

{
  "usuario_id": 1,
  "data": "2025-11-21",
  "entrada": "2025-11-21T01:18:33.764Z",
  "saida": "2025-11-21T01:18:33.764Z",
  "mensagem": "Registro efetuado"
}
