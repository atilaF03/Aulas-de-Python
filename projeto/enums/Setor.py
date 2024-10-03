from enum import Enum

class Setor(Enum):
    ENGENHEIRO=("Engenheiro")
    SAUDE = ("Saúde")
    JURIDICO=("Juridico")
    OPERACOES=("Operações")

    def __init__(self, nome:str) -> None:
        self.nome = nome