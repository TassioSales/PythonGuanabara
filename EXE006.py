from math import sqrt


def dobro():
    print(f'O dobro do numero {num} e {num * 2}')


def triplo():
    print(f'O triplo de {num} e {num * 3}')

def raiz():
    print(f'A raiz quadrada de {num} e {sqrt(num):.2f}')


num = int(input('Digite um numero:'))

dobro()
triplo()
raiz()
