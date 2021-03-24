from random import randint
from time import sleep

lista = []
jogos = []
print('-_-' * 8)
print('GERADOR JOGOS DA MEGA')
print('-_-' * 8)
qtd = int(input('Quantos jogos voce quer ?'))
tot = 0
while tot <= qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-x-' * 3, f'SORTEANDO {qtd} JOGOS', '-x-' * 3)
for i, l in enumerate(jogos):
    print(f'jogo {i + 1}: {l}')
    sleep(2)
print('-x-' * 3, '< BOA SORTE >', '-x-' * 3)

