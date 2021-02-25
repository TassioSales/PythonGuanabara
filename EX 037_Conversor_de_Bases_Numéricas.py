def binario(x):
    print(f"O numero {x} convertido para binario e {bin(x)[2:]}")

def octal(x):
    print(f'O numero {x} convertido para OCTAL e {oct(x)[2:]}')

def hexadecimal(x):
      print(f'O numero {x} convertido para HEXADECIMAL e {hex(x)[2:]}')

num = int(input('Digite um numero: '))
print('[ 1 ] converter para BINARIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opc = int(input('Digite sua opção: '))
if opc == 1:
    binario(num)
elif opc == 2:
    octal(num)
elif opc == 3:
    hexadecimal(num)
else:
    print("OPÇÃO INVALIDA")