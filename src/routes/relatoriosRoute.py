from fastapi import APIRouter, Depends
from typing import List
from typing import Optional
from auth.auth import auth_required
from controller.relatorioController import consultar_fretes, registrar_ponto
from schemas.relatorioSchema import RelatorioResponse
from schemas.pontoSchema import PontoRequest, PontoResponse

import datetime

router = APIRouter(prefix="/relatorio", tags=["Relatorio"])

@router.get("/fretes-dia", response_model=List[RelatorioResponse])
def route_consultar_frete(data_consulta: Optional[datetime.date] = None, user: dict = Depends(auth_required)):
    return consultar_fretes(data_consulta, user)

@router.post("/ponto", response_model=PontoResponse)
def route_ponto(req: PontoRequest, user: dict = Depends(auth_required)):
    return registrar_ponto(req, user)
