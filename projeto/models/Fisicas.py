import sys
sys.path.append("/workspaces/Python-Orientado-a-Objetos/")

from abc import ABC ,abstractmethod
from projeto.models.Endereco import Endereco
from projeto.enums.Genero import Genero
from projeto.models.Pessoa import Pessoa

class Fisica(Pessoa,ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco,cpf: str, rg: str,dataNascimento: str,sexo :Genero) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cpf= cpf
        self.rg= rg
        self.dataNascimento = dataNascimento
        self.sexo = sexo

    def __str__(self) -> str:
        return (f"\nsuper().__str__()"
                f"\no cpf: {self.cpf}"
                f"\no rg:{self.rg}"
                f"\ndata de nascimento{self.dataNascimento}"
                f"\no sexo é {Genero.name}"
                )
    