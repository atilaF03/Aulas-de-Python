from enums.UnidadeFederativa import UnidadeFederativa 

class Endereco():
    def __init__(self, logradouro: str,numero:str,complemento:str,cep:str,cidade:str, uf: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep 
        self.cidade = cidade
        self.uf= UnidadeFederativa

    def __str__(self) -> str:
        pass
