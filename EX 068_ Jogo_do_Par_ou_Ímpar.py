from random import randint
v = 0
while True:
    jogador = int(input("Digite seu numero: "))
    computador  = randint(0,10)
    total = computador + jogador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Escolha par = [ P ] ou impar = [ I ]: ")).strip().upper()[0]
    print(f"Voce jogou {jogador} o computador {computador} o total e {total}", end = " ")
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == "P":
        if total % 2 == 0:
            print("VOCE VENCEU")
            v += 1
        else:
            print("VOCE PERDEU")
            break

    elif tipo == "I":
        if total % 2 == 1:
                print("VOCE VENCEU")
                v += 1
        else:
            print("VOCE PERDEU")
            break
    print("Vamor jogar Novamente...")
print(f"GAME OVER VOCE JOGOU {v} VEZES")
            
