from pydantic import BaseModel
from typing import Optional
import datetime

class PontoRequest(BaseModel):
    tipo: str 

class PontoResponse(BaseModel):
    usuario_id: int
    data: datetime.date
    entrada: Optional[datetime.datetime]
    saida: Optional[datetime.datetime]
    mensagem: str
