from random import randint
from time import sleep


pc = randint(0, 5)
print("-=-" * 20)
print("Vou pensar em um numero entre 0 e 5. Tente adivinhar")
print("-=-" * 20)
jogador = int(input("Em que numero eu pensei ? "))
print("PROCESSANDO....")
sleep(3)
if pc == jogador:
    print("Parabens você acertou")
elif pc != jogador:
    print(f"Ganhei ! eu pensei no numero {pc} e nao no numero {jogador}")




