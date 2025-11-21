from datetime import datetime

class Funcionario:
    """
    Funcionário (gerente ou entregador).
    """

    def __init__(self, cargo: str, nome: str, numero_registro: str, senha: str):
        self._id = None
        self._cargo = cargo
        self._nome = nome
        self._numero_registro = numero_registro
        self._senha = senha
        
        # timestamps
        self._created_at = datetime.utcnow()
        self._updated_at = datetime.utcnow()

    # Getters
    @property
    def id(self): return self._id

    @property
    def cargo(self): return self._cargo

    @property
    def nome(self): return self._nome

    @property
    def numero_registro(self): return self._numero_registro

    @property
    def senha(self): return self._senha

    @property
    def created_at(self): return self._created_at

    @property
    def updated_at(self): return self._updated_at

    # Setters
    @id.setter
    def id(self, v): self._id = v

    @cargo.setter
    def cargo(self, v):
        self._cargo = v
        self._updated_at = datetime.utcnow()

    @nome.setter
    def nome(self, v):
        self._nome = v
        self._updated_at = datetime.utcnow()

    @numero_registro.setter
    def numero_registro(self, v):
        self._numero_registro = v
        self._updated_at = datetime.utcnow()

    @senha.setter
    def senha(self, v):
        self._senha = v
        self._updated_at = datetime.utcnow()
