## AQUI SERÁ ADICIONADA A LÓGICA DE NEGÓCIO - CALCULO DO FRETE
from model.frete import Frete
import requests
from repository.freteRepository import inserir_frete
from fastapi import HTTPException
from repository.freteRepository import atualizar_status, obter_frete_por_id, listar, buscar_frete
from repository.relatorioRepository import verificar_cargo
from schemas.consultarFreteSchema import FreteConsultaResponse

def gerar_frete(peso, distancia, opcao, cep_origem, cep_destino, user_id: int) -> str:
    
        if opcao == 1:
            frete = Frete(distancia, peso)
            frete.tipo = "Normal"
            frete.calcular_preco()
        elif opcao == 2:
            frete = Frete(distancia, peso)
            frete.tipo = "Sedex"
            frete.calcular_preco()
        elif opcao == 3:
            frete = Frete(distancia, peso)
            frete.tipo = "Sedex10"
            frete.calcular_preco()

        frete_id = inserir_frete(
            user_id=user_id,
            tipo=frete.tipo,
            valor=frete.valor,
            distancia=frete.distancia,
            peso=frete.peso,
            status="solicitado",
            cep_origem=cep_origem,
            cep_destino=cep_destino
        )

        return {
            "frete_id": frete_id,
            "valor": frete.valor,
            "tipo": frete.tipo,
            "status": "solicitado"
        }

def validar_ceps(cep_origem, cep_destino) -> str:
    url_cep_origem = f"https://brasilapi.com.br/api/cep/v2/{cep_origem}"
    url_cep_destino = f"https://brasilapi.com.br/api/cep/v2/{cep_destino}"

    res_origem = requests.get(url_cep_origem)

    if res_origem.status_code != 200:
        raise Exception(f"CEP de origem inválido: {cep_origem}")
    
    dados_origem = res_origem.json()

    res_destino = requests.get(url_cep_destino)

    if res_destino.status_code != 200:
        raise Exception(f"CEP de destino inválido: {cep_destino}")
    
    dados_destino = res_destino.json()

    return {
        "origem": dados_origem ,
        "destino": dados_destino
    }

def calcular_distancia(dados_ceps) -> str:
    try:
        latitude_origem = dados_ceps['origem']['location']['coordinates']['latitude']
        longitude_origem = dados_ceps['origem']['location']['coordinates']['longitude']

        latitude_destino = dados_ceps['destino']['location']['coordinates']['latitude']
        longitude_destino = dados_ceps['destino']['location']['coordinates']['longitude']

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e} - BrasilAPI não localizou as coordenadas geográficas")

    coordenadas = f"{longitude_origem},{latitude_origem};{longitude_destino},{latitude_destino}"

    url = f"http://router.project-osrm.org/route/v1/driving/{coordenadas}?overview=false"
    res = requests.get(url)
    resposta = res.json()

    distancia = resposta["routes"][0]["distance"]
    distancia_km = float(f"{distancia/1000:.1f}")

    return distancia_km

def pagamento(req, user_id: int):
    print('FRETE_ID: ', req.frete_id)
    print('USER ID: ', user_id)

    frete = obter_frete_por_id(req.frete_id)
    print(' FRETE: ', frete)

    if not frete:
        raise HTTPException(status_code=404, detail="Frete não encontrado")

    if frete["usuario_id"] != user_id['id']:
        raise HTTPException(status_code=403, detail="Você não tem permissão")

    if frete["status"] != "solicitado":
        raise HTTPException(status_code=400, detail=f"Pagamento não permitido. Status atual: {frete['status']}")

    atualizar_status(req.frete_id, "enviado", req.meio_pagamento)

    return {
        "frete_id": req.frete_id,
        "status": "enviado",
        "meio_pagamento": req.meio_pagamento
    }

def historico(user_id: int):
    fretes = listar(user_id)

    return {
        "fretes": fretes
    }

def consultar_frete_service(frete_id, user):
    cargo = verificar_cargo(user["id"])

    if cargo != "entregador":
        raise HTTPException(status_code=403, detail="Apenas entregadores podem consultar detalhes do frete")

    try:
        frete = buscar_frete(frete_id)
        if not frete:
            raise HTTPException(status_code=404, detail="Frete não encontrado")

        return FreteConsultaResponse(
            cep_origem=frete["cep_origem"],
            cep_destino=frete["cep_destino"],
            nome_remetente=frete["nome"],
            telefone_remetente=frete["telefone"]
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
