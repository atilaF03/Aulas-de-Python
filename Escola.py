

def calcularMedia(nota1 :float, nota2:float,nota3:float):
    res = (nota1 + nota2 + nota3)/3
    print(res)
    return res

class Aluno:
    def __init__(self,nome:str, idade:int, sexo) -> None:
        self.nome= nome
        self.idade= idade
        self.sexo= sexo
    
    def __str__(self) -> str:
        return(f"\n{self.nome}"
               f"\n{self.idade}"
               f"\n{self.sexo}"
               )


num1 = float(input("insira a primeira nota"))

num2 = float(input("insira a segunda nota"))

num3 = float(input("insira a terceira nota nota"))

media = calcularMedia(num1,num2,num3)

aluno1 = Aluno("atila",24,"macho")
print(aluno1)
print(f"as notas do aluno foram \n{num1}\n{num2},\n{num3}\n a média do aluno foi: {media}")