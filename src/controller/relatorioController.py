from fastapi import HTTPException
from service.relatorioService import consultar_fretes_service, registrar_ponto_service

def consultar_fretes(req, user):
    try:
        return consultar_fretes_service(req, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def registrar_ponto(req, user):
    try:
        return registrar_ponto_service(req, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

