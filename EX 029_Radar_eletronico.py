vel = int(input("Qual a velocidade do carro ? "))
velMaxima = 80
if vel > 80:
    print(f"Sua velocidade atual e {vel}Km/h e voce esta acima de velocidade maxima que e {velMaxima}Km/h")
    print("MULTADO")
    print(f"Tera que pagar um multa de R$ {(vel - velMaxima) *  7}")
else:
    print("Sua velocidade esta dentro dos padroes de segurança")
print("Tenha um bom dia! Dirija com segurança")

