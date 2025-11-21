from fastapi import HTTPException
from service import freteService

def calcular_frete(req, user: dict):
    try:
        dados_cep = freteService.validar_ceps(req.cep_origem, req.cep_destino)

        distancia = freteService.calcular_distancia(dados_cep)
        
        return freteService.gerar_frete(req.peso, distancia, req.opcao, req.cep_origem, req.cep_destino, user_id=user["id"])

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
def pagamento(req, user: dict):
    try:
        return freteService.pagamento(req, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
def historico(user: dict):
    try:
        return freteService.historico(user["id"])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def consultar_frete(frete_id, user: dict):
    print('FRETE ID: ', frete_id)
    try:
        return freteService.consultar_frete_service(frete_id, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))