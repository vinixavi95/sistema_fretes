from pydantic import BaseModel

class UsuarioRequest(BaseModel):
    nome: str
    email: str
    senha: str
    telefone: int
    eh_funcionario: bool

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    mensagem: str
