from pydantic import BaseModel

class FreteRequest(BaseModel):
    peso: float
    opcao: int
    cep_origem: str
    cep_destino: str

class FreteResponse(BaseModel):
    frete_id: int
    valor: float
    tipo: str
    status: str #calculado, pendente e enviado#
