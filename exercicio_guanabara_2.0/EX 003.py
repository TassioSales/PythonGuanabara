num1 = float(input('Digite uma numero: '))
num2 = float(input('Digite outro numero: '))


def soma(x, y): return x + y
def subtracao(x, y): return x - y
def divisao(x, y): return x / y
def multiplicacao(x, y): return x * y


print(f'''{'MENU':^20}
      [ 1 ] SOMA
      [ 2 ] SUBTRAÇÃO 
      [ 3 ] DIVISAO
      [ 4 ] MULTIPLICAÇÃO
      [ 5 ] SAIR ''')
opc = int(input('digite a opção desejada: '))
if opc == 1:
    print(f'A soma de {num1} e {num2} = {soma(num1, num2)}')
elif opc == 2:
    print(f'A subtração de {num1} e {num2} = {subtracao(num1, num2)}')
elif opc == 3:
    print(f'A divisao de {num1} e {num2} = {divisao(num1, num2)}')
elif opc == 4:
    print(f'A multiplicação de {num1} e {num2} = {multiplicacao(num1, num2)}')
else:
    print('opção invalida')
