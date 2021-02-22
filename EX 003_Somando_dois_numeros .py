def soma():
    print(f'A soma de {num1} + {num2} = {num1 + num2}')


def subtracao():
    print(f'A soma de {num1} - {num2} = {num1 - num2}')


def divisao():
    print(f'A soma de {num1} / {num2} = {num1 / num2}')


def multiplicacao():
    print(f'A soma de {num1} X {num2} = {num1 * num2}')


num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
print("*X" * 16)
print("X*" * 5, "OPERADORES", "*X" * 5)
print("*X" * 16)
print('(1) soma\n'
      '(2) subtração\n'
      '(3) divisão\n'
      '(4) Multiplicação\n')
opcao = int(input('Qual opcão ?'))
if opcao == 1:
    soma()
elif opcao == 2:
    subtracao()
elif opcao == 3:
    divisao()
elif opcao == 4:
    multiplicacao()
