jogador = dict()
partidas = list()

jogador['nome'] = str(input('Qual nome do jogador ? '))
totpartidas = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou ? '))
for c in range(0, totpartidas):
    partidas.append(int(input(f'Quantos gols na partida {c + 1} ?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('x' * 62)
print(jogador)
print('x' * 62)
for k, v in jogador.items():
    print(f'o Campo {k} tem o valor {v}')
print('x' * 62)
print(f'O jogador {jogador["nome"]} jogou  {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i + 1} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
