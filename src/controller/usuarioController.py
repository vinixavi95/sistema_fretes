from fastapi import HTTPException
from service.usuarioService import autenticar_usuario, atualizar_usuario, criar_usuario, criar_funcionario

def cadastrar(req):
    try:
        novo_usuario = criar_usuario(req)
        return novo_usuario
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
def logar(req):
    try:
        return autenticar_usuario(req)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
def atualizar(req, user):
    try:
        return atualizar_usuario(req, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
def cadastrar_funcionario(req, user):
    try:
        return criar_funcionario(req, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
