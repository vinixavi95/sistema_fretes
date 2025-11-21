from pydantic import BaseModel

class HistoricoRequest(BaseModel):
    usuario_id: int

class HistoricoResponse(BaseModel):
    fretes: list