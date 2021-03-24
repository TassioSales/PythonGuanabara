num = [[], []]
valor = 0
qtd = int(input("Quantas numeros deseja cadastrar ? "))
for c in range(0, qtd):
    valor = (int(input(f'Digite o {c + 1}: ')))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print("X" * 30)
print(f'{num}')
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores impares digitados foram {num[1]}')