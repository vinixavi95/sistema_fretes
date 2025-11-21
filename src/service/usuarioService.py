from fastapi import HTTPException
from schemas.usuarioSchema import UsuarioResponse
from model.usuario import Usuario
from repository.usuarioRepository import buscar, obter_usuario_por_id, atualizar_usuario_bd, inserir, inserir_funcionario, buscar_status
from auth.auth import create_token
from schemas.loginSchema import LoginRequest, LoginResponse
from utils.hash import hash_password
from utils.hash import verify_password
from schemas.funcionarioSchema import FuncionarioRequest, FuncionarioResponse

def criar_usuario(req):
    senha_hash = hash_password(req.senha)

    try:
        usuario = Usuario(
            nome=req.nome,
            telefone=req.telefone,
            email=req.email,
            senha=senha_hash,
            eh_funcionario=req.eh_funcionario
        )

        result = inserir(
            nome=usuario.nome,
            email=usuario.email,
            telefone=usuario.telefone,
            senha=usuario.senha,
            eh_funcionario=usuario.eh_funcionario
        )

        return UsuarioResponse(
            id=result[0],
            nome=result[1],
            email=result[2],
            mensagem="Usuário criado com sucesso!"
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def autenticar_usuario(req):
    usuario = buscar(req.email)

    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")

    if not verify_password(req.senha, usuario['senha']):
        raise HTTPException(status_code=401, detail="Senha incorreta")

    token = create_token({"id": usuario['id'], "email": req.email})

    return LoginResponse(access_token=token, token_type= "Bearer")

def atualizar_usuario(req, user):
    usuario = obter_usuario_por_id(user['id'])

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    nome = req.nome if req.nome else usuario["nome"]
    email = req.email if req.email else usuario["email"]
    senha = hash_password(req.senha) if req.senha else usuario["senha"]

    atualizar_usuario_bd(user['id'], nome, email, senha)

    return {
        "id": user['id'],
        "nome": nome,
        "email": email,
        "mensagem": "Dados atualizados com sucesso."
    }

def criar_funcionario(req: FuncionarioRequest, user):
    try:
        eh_funcionario = buscar_status(req.usuario_id)
    except:
        raise HTTPException(status_code=404, detail=f"Usuário ID {req.usuario_id} não encontrado na base de usuários.")
    
    if not eh_funcionario:
        raise HTTPException(
            status_code=403, 
            detail="Acesso negado. Usuário não está sinalizado como funcionário na tabela 'usuarios'."
        )

    try:
        result = inserir_funcionario(
            usuario_id=req.usuario_id,
            cargo=req.cargo,
            numero_registro=req.numero_registro
        )

        return FuncionarioResponse(
            usuario_id=result[0],
            cargo=result[1],
            mensagem="Dados de funcionário cadastrados com sucesso!"
        )
        
    except Exception as e:
        raise e