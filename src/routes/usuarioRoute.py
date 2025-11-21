from fastapi import APIRouter, Depends
from auth.auth import auth_required
from controller.usuarioController import cadastrar, logar, atualizar, cadastrar_funcionario
from schemas.usuarioSchema import UsuarioRequest, UsuarioResponse
from schemas.loginSchema import LoginRequest, LoginResponse
from schemas.usuarioUpdateSchema import UsuarioUpdateRequest, UsuarioUpdateResponse
from schemas.funcionarioSchema import FuncionarioRequest, FuncionarioResponse

router = APIRouter(prefix="/usuario", tags=["Usuario"])

@router.post("/cadastro", response_model=UsuarioResponse)
def cadastro(req: UsuarioRequest):
    return cadastrar(req)

@router.post("/login", response_model=LoginResponse)
def login(req: LoginRequest):
    return logar(req)

@router.put("/atualizar", response_model=UsuarioUpdateResponse)
def route_atualizar_usuario(req: UsuarioUpdateRequest, user: dict = Depends(auth_required)):
    return atualizar(req, user)

@router.post("/funcionario", response_model=FuncionarioResponse)
def route_cadastrar_funcionario(req: FuncionarioRequest, user: dict = Depends(auth_required)):
    return cadastrar_funcionario(req, user)