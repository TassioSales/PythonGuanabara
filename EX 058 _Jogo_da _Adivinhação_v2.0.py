from random import randint
pc = randint(0, 10)
cont = 0

while True:
    usuario = int(input("Digite o numero que você pensou: "))
    if usuario == pc:
        cont += 1
        break
    else:
        if pc > usuario:
            print("Maior...Tente novamente")
            cont += 1
        elif pc < usuario:
            print("Menor...Tente novamente")
            cont += 1
print(f"Parabens voce acertou na {cont}º tentativa")