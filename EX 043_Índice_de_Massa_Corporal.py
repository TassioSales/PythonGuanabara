peso =  float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc  =  peso / (altura**2)

print(f'Seu imc e {imc:.2f}')

if imc < 18.5:
    print("Classificação: Abaixo do Peso")
elif 18.5 <= imc < 25:
    print("Classificação: Normal")
elif 25  <= imc < 30:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 40:
    print("Classificação: Obesidade")
else:
    print("Classificação: Obesidade Mórbida")
