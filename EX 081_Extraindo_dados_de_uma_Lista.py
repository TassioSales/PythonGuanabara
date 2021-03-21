lista = []
cont = 0

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    cont += 1
    opc = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if opc == 'S':
        continue
    elif opc == 'N':
        break
    else:
        print('Opção invalida')
print(f'Voce digitou {cont} numeros')
lista.sort(reverse=True)
print(f'A Lista ordenada e {lista}')
if 5 in lista:
    print("O numero 5 foi encontrado")
else:
    print('O Numero 5 nao foi encontrado')
