import sys
sys.path.append("/workspaces/Python-Orientado-a-Objetos/")


from abc import ABC ,abstractmethod
from projeto.models.Endereco import Endereco

class Pessoa(ABC):

    def __init__(self, nome :str, telefone: str , email: str, endereco : Endereco) -> None:
      self.nome = nome 
      self.telefone = telefone 
      self.email =email
      self.endereco = endereco

    def __str__(self) -> str:
        return(f"o nome:{self.nome}"
               f"o telefone é:{self.telefone}"
               f"o email é :{self.email}"
               f"o endereco é {self. endereco }"
               )