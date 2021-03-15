times = ('Flamengo', 'Internacional', 'Atlético Mineiro', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos'
         , 'Atlético Paranaense', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético Goianiense', 'Bahia', 'Sport',
         'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')

print(f"Lista de times Braileirao: {times}")
print('X' * 25)
print(f'Os 5 primeiros são {times[0:5]}')
print('X' * 25)
print(f'Os ultimos 4 são {times[-4:]}')
print('Os times em ordem alfabetica:')
print(f'{sorted(times)}', end=" ")
print('X' * 25)
print(f'O coritiba esa na posição {times.index("Coritiba") + 1}ª posição')
