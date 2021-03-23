lista = []
pares = []
impar = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    opc = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if opc == 'S':
        continue
    elif opc == 'N':
        break
    else:
        print('Opção invalida')
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)
print(f'Lista completa {lista}')
print(f'Lista de pares {pares}')
print(f'Lista de impares {impar}')
