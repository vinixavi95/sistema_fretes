from pydantic import BaseModel

class FuncionarioRequest(BaseModel):
    usuario_id: int
    cargo: str
    numero_registro: int

class FuncionarioResponse(BaseModel):
    usuario_id: int
    cargo: str
    mensagem: str