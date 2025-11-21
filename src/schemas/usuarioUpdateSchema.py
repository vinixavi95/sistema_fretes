from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UsuarioUpdateRequest(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None

class UsuarioUpdateResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    mensagem: str
