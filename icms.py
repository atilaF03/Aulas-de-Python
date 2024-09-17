

nome = str(input("digite seu nome: "))
altura= float(input("digite sua altura: "))
peso = float(input("digite seu peso: "))

imc = peso / (altura**2)
print(
      f"\nseu nome é{nome}"
      f"\no seu imc é: {imc:.2f}"# faz aparecer só duas casas decimais
      f"\nseu peso é {peso:.2f}"
      f"\nsua altura é {altura:.2f}"
     )