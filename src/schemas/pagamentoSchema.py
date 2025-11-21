from pydantic import BaseModel

class PagamentoRequest(BaseModel):
    frete_id: int
    meio_pagamento: str

class PagamentoResponse(BaseModel):
    frete_id: int
    status: str
    meio_pagamento: str