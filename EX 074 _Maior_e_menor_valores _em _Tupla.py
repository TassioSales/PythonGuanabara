from random import randint

valores = [randint(1, 60) for i in range(0, 6)]

print(f'Os valores sorteado foram', end=" ")

valores = sorted(valores)

for n in valores:
    print(f'{n}', end=" ")

print(f"\nO Maior valor sorteado foi {max(valores)}")
print(f'O menor valor sorteado foi {min(valores)}')
