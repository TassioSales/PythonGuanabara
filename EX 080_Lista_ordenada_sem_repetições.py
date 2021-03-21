lista = list()

for c in range(0, 5):
    n = int(input(f"Digite o {c + 1}ª valor: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionada no fim da lista ')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista ')
                break
            pos += 1
print(f'Os valores digitados em ordem são {lista}')
print(sorted(lista))