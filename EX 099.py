from time import sleep

def maior(*num):
    cont = maior = 0
    print('\nanalisando os valores passados...\n')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nforam imformado {cont} valores')
    print(f'\no maior valor informado for {maior}')


maior(8,5,6,9,1,2)
maior(7,6,3,4,5)
maior(8,2,1,3,)
maior(1,2,4)
maior(3,5)
maior(9)
maior()

