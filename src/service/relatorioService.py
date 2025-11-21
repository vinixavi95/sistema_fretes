from fastapi import HTTPException
from schemas.relatorioSchema import RelatorioResponse
from schemas.pontoSchema import PontoResponse
from model.usuario import Usuario
from repository.relatorioRepository import verificar_cargo, listar, buscar_ponto_do_dia, inserir_entrada, inserir_saida

import datetime

def consultar_fretes_service(data_consulta, user):
    cargo = verificar_cargo(user['id'])

    if cargo != 'gerente':
        raise HTTPException(status_code=403, detail="Apenas gerentes podem acessar o relatório")
    
    try:
        data = data_consulta or datetime.date.today()
        fretes = listar(data)
        print('FRETES: ', fretes)
        itens = [
            RelatorioResponse(
                frete_id=f[0],
                status=f[1],
                valor=f[2],
                meio_pagamento=f[3],
                mensagem=f"Lista de fretes do dia : {data}"
            )
            for f in fretes
        ]

        return itens
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
def registrar_ponto_service(req, user):
    cargo = verificar_cargo(user["id"])
    
    if cargo not in ["gerente", "entregador"]:
        raise HTTPException(status_code=403, detail="Apenas gerentes e entregadores podem bater ponto")

    hoje = datetime.date.today()
    ponto = buscar_ponto_do_dia(user["id"], hoje)

    if req.tipo == "entrada":
        if ponto and ponto["entrada"] is not None:
            raise HTTPException(status_code=400, detail="Entrada já registrada")

        ponto = inserir_entrada(user["id"], hoje)

        return PontoResponse(
            usuario_id=user["id"],
            data=hoje,
            entrada=ponto["entrada"],
            saida=ponto.get("saida"),
            mensagem="Ponto de ENTRADA registrado com sucesso"
        )

    elif req.tipo == "saida":
        if not ponto or ponto["entrada"] is None:
            raise HTTPException(status_code=400, detail="Necessário registrar entrada antes da saída")

        if ponto["saida"] is not None:
            raise HTTPException(status_code=400, detail="Saída já registrada")

        ponto = inserir_saida(ponto["id"])

        return PontoResponse(
            usuario_id=user["id"],
            data=hoje,
            entrada=ponto["entrada"],
            saida=ponto["saida"],
            mensagem="Ponto de SAÍDA registrado com sucesso"
        )

    else:
        raise HTTPException(status_code=400, detail="Tipo inválido (use 'entrada' ou 'saida')")