from random import randint
from time import sleep

def Pedra(jogador):
    if jogador == 0:
            print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")  
    elif jogador == 2:
        print("COMPUTADOR VENCE")   
    else:
        print("JOGADA INVALIDA")

def Papel(jogador):
    if jogador == 0:
        print("COMPUTADOR VENCE") 
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE") 
    else:
        print("JOGADA INVALIDA")

def Tesoura(jogador):
    if jogador == 0:
            print("JOGADOR VENCE")     
    elif jogador == 1:
        print("COMPUTADOR VENCE") 
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVALIDA")

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print("[ 0 ] PEDRA\n"
      "[ 1 ] PAPEL\n"
      "[ 2 ] TESOURA\n")

jogador = int(input("Qual sua jogada ?"))
sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)

print('-=-' * 12)
print(f"O computador escolheu {itens[computador]}")
print(f"O jogador escolheu {itens[jogador]}")
print('-=-' * 12)

if computador == 0:
    Pedra(jogador)

elif computador == 1:
    Papel(jogador)

elif computador == 2:
    Tesoura(jogador)

