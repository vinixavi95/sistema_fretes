class Usuario:
    """
    Modelo de domínio para Usuário (cliente do sistema).
    Este objeto representa somente a entidade na camada de negócio.
    Persistência (inserir/atualizar no banco) deve ser feita em repository.
    """

    def __init__(self, nome: str, telefone: str, email: str, senha: str, eh_funcionario: bool ):
        self._id = None
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._senha = senha  
        self._eh_funcionario = eh_funcionario
        
    # Getters
    @property
    def id(self) -> int:
        return self._id

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def telefone(self) -> str:
        return self._telefone

    @property
    def email(self) -> str:
        return self._email

    @property
    def senha(self) -> str:
        return self._senha
    
    @property
    def eh_funcionario(self) -> bool: # <--- NOVO GETTER
        return self._eh_funcionario

    # Setters
    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @telefone.setter
    def telefone(self, telefone: str) -> None:
        self._telefone = telefone

    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    @senha.setter
    def senha(self, senha: str) -> None:
        self._senha = senha
    
