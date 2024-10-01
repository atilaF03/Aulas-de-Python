class Aluno:
      """ atributos de classe"""
      def __init__(self, nome:str, idade:int,cpf : str) -> None:
           self.nome = nome
           self. idade = idade 
           self.cpf = cpf
           """ to string python version """
      def __str__(self) -> str:
           return (f"\n o nome do aluno é: {self.nome}"
                   f"\n a idade do aluno é: {self.idade}"
                   f"\n o cpf do aluno é {self.idade}"
                   )
    #instanciando objetos
aluno = Aluno("atila", 23,"896-963-963-04")
print(aluno)