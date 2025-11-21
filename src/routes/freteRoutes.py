from fastapi import APIRouter, Depends, HTTPException
from controller.freteController import calcular_frete, pagamento, historico, consultar_frete
from schemas.freteSchema import FreteRequest, FreteResponse
from auth.auth import auth_required
from schemas.pagamentoSchema import PagamentoRequest, PagamentoResponse
from schemas.historicoSchema import HistoricoRequest, HistoricoResponse
from schemas.consultarFreteSchema import FreteConsultaResponse

router = APIRouter(prefix="/frete", tags=["Frete"])

@router.post("/solicitacao", response_model=FreteResponse)
def route_calcular_frete(req: FreteRequest, user: dict = Depends(auth_required)):
    return calcular_frete(req, user)

@router.post("/pagamento", response_model=PagamentoResponse)
def route_pagamento(req: PagamentoRequest, user: dict = Depends(auth_required)):
    return pagamento(req, user)

@router.get("/historico", response_model=HistoricoResponse)
def route_historico(user: dict = Depends(auth_required)):
    return historico(user)

@router.get("/consulta", response_model=FreteConsultaResponse)
def route_consultar_frete(frete_id: int, user: dict = Depends(auth_required)):
    return consultar_frete(frete_id, user)