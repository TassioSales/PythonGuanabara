def soma():
    for c in range(posicaoInicial, posicaoFinal + 1):
        print(f"{num} + {c} = {num + c}")
    print("\n\n")


def subtracao():
    for c in range(posicaoInicial, posicaoFinal + 1):
        print(f'{num} - {c} = {num - c}')
    print("\n\n")


def multiplicacao():
    for c in range(posicaoInicial, posicaoFinal + 1):
        print(f'{num} X {c} = {num * c}')
    print("\n\n")


def todos():
    for c in range(posicaoInicial, posicaoFinal + 1):
        print(f"{num} + {c} = {num + c}")
    print("\n")
    for c in range(posicaoInicial, posicaoFinal + 1):
        print(f'{num} - {c} = {num - c}')
    print("\n")
    for c in range(posicaoInicial, posicaoFinal + 1):
        print(f'{num} - {c} = {num - c}')


while True:
    num = int(input('Digite aqui o numero que voce que ver a tabuada: '))
    posicaoInicial = int(input('Em que numero deseja iniciar a conta: '))
    posicaoFinal = int(input("Em que numero deseja terminar: "))
    if posicaoFinal <= posicaoFinal:
        while posicaoFinal <= posicaoInicial:
            print("Numero final menor ou igual a numero inicial: ")
            posicaoFinal = int(input("Em que numero deseja terminar: "))

    print('I-I' * 10)
    print('I-I' * 3, 'OPERADORES', 'I-I' * 3)
    print('I-I' * 10)
    print('( 1 ) SOMA\n'
          '( 2 ) SUBTRAÇÃO\n'
          '( 3 ) MULTIPLICAÇÃO\n'''
          '( 4 ) TODOS\n'
          '( 5 ) SAIR')

    opcao = int(input('Qual OPÇÃO vai usar ?'))

    if opcao == 1:
        soma()
    elif opcao == 2:
        subtracao()
    elif opcao == 3:
        multiplicacao()
    elif opcao == 4:
        todos()
    elif opcao == 5:
        break
    else:
        print("Opção invalida")
