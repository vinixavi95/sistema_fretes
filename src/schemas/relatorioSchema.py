from pydantic import BaseModel

class RelatorioResponse(BaseModel):
    frete_id: int 
    status: str
    valor: float
    meio_pagamento: str
    mensagem: str
