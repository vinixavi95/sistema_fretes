from pydantic import BaseModel

class FreteConsultaResponse(BaseModel):
    cep_origem: str
    cep_destino: str
    nome_remetente: str
    telefone_remetente: str
