**#📦 Sistema de Fretes — Backend (FastAPI)**

Este projeto implementa um servidor backend completo para o sistema de fretes, permitindo que usuários se autentiquem, solicitem fretes, realizem pagamentos, consultem históricos e acessem relatórios conforme seu cargo (gerente, entregador ou usuário comum).

A API foi construída com FastAPI, executada via Uvicorn, utiliza PostgreSQL como banco de dados e integra com duas APIs externas:

- BrasilAPI — consulta de CEP e coordenadas

- Project OSRM — cálculo de distância geográfica



##🚀 Funcionalidades Implementadas

###👤 Usuário

Cadastro

Login (gera token JWT)

Atualização de dados

Solicitação de frete

Pagamento de frete

Histórico de fretes


###🧑‍💼 Funcionário

Cadastro como funcionário (após criar conta)

Consulta de fretes por entregadores

Relatórios de fretes por gerentes

Registro de ponto (entrada/saída)


###🗄️ Estrutura da API (Architecture)

O projeto segue a separação clara de responsabilidades:


route → controller → service → repository



route: recebe requisições HTTP

controller: valida e orquestra chamadas

service: regras de negócio

repository: acesso ao banco de dados


###🛠️ Tecnologias

Python 3.13

FastAPI

Uvicorn

PostgreSQL

psycopg2

python-jose (JWT)

API BrasilAPI

API OSRM


##▶️ Como executar o projeto

###1. Clone o repositório

git clone https://github.com/vinixavi95/sistema_fretes.git

cd sistema_fretes


###2. Instalação das dependências (opcional sem Docker)

Se você quiser rodar o projeto localmente sem Docker, use um ambiente virtual e instale as dependências via requirements.txt:

Criar e ativar um ambiente virtual
python -m venv venv

No Linux/macOS
source venv/bin/activate

No Windows
venv\Scripts\activate

Instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

###3. Rodar o projeto

####Com Docker (recomendado)

A imagem Docker já inclui o PostgreSQL e o esquema do banco de dados. Para subir tudo, execute:

docker compose up --build

Isso criará e iniciará os containers do backend e do banco de dados.


####Sem Docker

Se estiver usando o ambiente virtual local, inicie o servidor FastAPI:

uvicorn main:app --reload


O servidor ficará disponível em http://127.0.0.1:8000.

###4. Acessar a documentação automática

O FastAPI fornece uma interface Swagger interativa:

http://127.0.0.1:8000/docs

##🗄️ Banco de Dados

O sistema utiliza PostgreSQL:

Com Docker: já vem configurado e inicializado junto com a aplicação.

Sem Docker: configure um PostgreSQL local e crie o banco conforme o script fretes.sql.


##🔐 Fluxo de Autenticação

Para usar a API, siga esta ordem:

Cadastro → cria o usuário

Login → gera o token

Usar o token → enviar no header como:

Authorization: Bearer <seu_token>


##🔑 Endpoints — Detalhamento Completo

###1. 👤 Cadastro de Usuário

POST /usuario/cadastro

Corpo da requisição:
{
  "nome": "string",
  "email": "string",
  "senha": "string",
  "telefone": 11999999999,
  "eh_funcionario": false
}


###2. 🔑 Login

POST /usuario/login

Corpo:
{
  "email": "string",
  "senha": "string"
}

Retorno:
{
  "access_token": "string",
  "token_type": "bearer"
}


###3. 🧑‍💼 Cadastro de Funcionário

POST /usuario/funcionario

Requer token de autenticação.

Corpo:
{
  "usuario_id": 1,
  "cargo": "gerente",
  "numero_registro": 12345
}


###4. ✏️ Atualizar Usuário

PUT /usuario/atualizar

Corpo:
{
  "nome": "string",
  "email": "user@example.com",
  "senha": "string"
}


##🚚 Frete — Solicitação, Pagamento e Histórico

###5. 📦 Solicitação de Frete

POST /frete/solicitacao

Requer token.

Corpo:
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


⚠️ Observação: A BrasilAPI apresenta instabilidades na devolução de coordenadas geográficas.
Quando isso ocorre, o cálculo da distância falha e o frete não pode ser calculado.

###6. 💳 Pagamento do Frete

POST /frete/pagamento

Corpo:
{
  "frete_id": 1,
  "meio_pagamento": "pix"
}

Retorno:
{
  "frete_id": 1,
  "status": "enviado",
  "meio_pagamento": "pix"
}

###7. 📜 Histórico de Fretes

GET /frete/historico

Acessível apenas para gerentes.

Retorno:
{
  "fretes": [
    "..."
  ]
}


###8. 🔍 Consulta de Frete (Entregador)

GET /frete/consulta?frete_id=1

Acesso restrito ao cargo entregador.

Retorno:
{
  "cep_origem": "string",
  "cep_destino": "string",
  "nome_remetente": "string",
  "telefone_remetente": "string"
}

##📊 Relatórios

###9. 📅 Fretes do Dia

GET /relatorio/fretes-dia?data_consulta=YYYY-MM-DD (opcional)

Se não passar data, retorna os fretes do dia atual.

Retorno:
[
  {
    "frete_id": 1,
    "status": "pago",
    "valor": 40,
    "meio_pagamento": "pix",
    "mensagem": "OK"
  }
]


###10. ⏱️ Registro de Ponto

POST /relatorio/ponto

Corpo:
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
