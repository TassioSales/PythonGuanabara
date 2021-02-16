from time import sleep

def contador(i, f, p):
    print(f'A contagem de {i} ate {f} de {p} em {p}\n')
    print()
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
    

contador(1, 10, 1)
contador(10, 0, 2)
print('\n')

inicio = int(input('INICIO: '))
fim = int(input('FIM: '))
intervalo = int(input('INTERVALO: '))

contador(inicio, fim, intervalo)