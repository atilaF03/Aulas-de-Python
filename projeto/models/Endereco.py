import sys
sys.path.append("/workspaces/Python-Orientado-a-Objetos/")
from projeto.enums.UnidadeFederativa import UnidadeFederativa 

class Endereco():
    def __init__(self, logradouro: str,numero:str,complemento:str,cep:str,cidade:str, uf: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep 
        self.cidade = cidade
        self.uf= uf 

    def __str__(self) -> str:
        return (f"\no logradouro é: {self.logradouro}"
                f"\no número é: {self.numero}"
                f"\no complemento é {self.complemento}"
                f"\no cep é {self.cep}"
                f"\na cidade é {self.cidade}"
                f"\n a unidade federativa é {self.uf}"
                )

endereco = Endereco("logradouro", "number","complemento", "cep","cidade",UnidadeFederativa.BAHIA.sigla)
print(endereco)