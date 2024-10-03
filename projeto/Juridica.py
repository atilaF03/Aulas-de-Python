from projeto.models.Endereco import Endereco
from projeto.models.Pessoa import Pessoa


class Juridica(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cnpj:str , inscricaoEstadual :str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricao= inscricaoEstadual
        
    def __str__(self) -> str:
        return (f"Pessoa juridica"
                f"\n{super().__str__()}"
                f"\n{self.cnpj}"
                f"\n{self.inscricao}"
                )