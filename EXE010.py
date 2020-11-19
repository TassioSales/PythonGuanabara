# dolar = (franco[1], euro[2], iene[3], rublo[4], real[5] )
USD = (1.09647, 1.18611, 0.00957115, 0.0130646, 0.184561)
# franco = (dolar[1], euro[2], iene[3], rublo[4], real[5])
CHF = (0.912088, 1.08190, 0.00872883, 0.0119166, 0.168380)
# euro = (dolar[1], franco[2], iene[3], rublo[4], real[5])
EUR = (0.843038, 0.924249, 0.00806778, 0.0110138, 0.155594)
# iene = (dolar[1], franco[2], euro[3], rublo[4], real[5] )
JPY = (104.493, 114.549, 123.939, 1.36509, 19.2881)
# rublo (dolar[1], franco[2], euro[3], iene[4], real[5])
RUB = (76.5400, 83.9150, 90.7922, 0.732615, 14.1297)
# real = (dolar[1], franco[2], euro[3], iene[4], rublo[5])
REAL = (5.41665, 5.93738, 6.43010, 0.0518823, 0.0708227)


def Dolar():
    if opc == 2:
        print(f'O valor em Franco {moeda} convertido para Dolar e {moeda * USD[0]:.2f}')
    elif opc == 3:
        print(f'O valor em Euro {moeda} convertido para Dolar e {moeda * USD[1]:.2f}')
    elif opc == 4:
        print(f'O valor em Iene {moeda} convertido para Dolar e {moeda * USD[2]:.2f}')
    elif opc == 5:
        print(f'O valor em Rublo {moeda} convertido para Dolar e {moeda * USD[3]:.2f}')
    elif opc == 6:
        print(f'O valor em Real{moeda} convertido para Dolar e {moeda * USD[4]:.2f}')


def Franco():
    if opc == 1:
        print(f'O valor em Dolar {moeda} convertido para Franco e {moeda * CHF[0]:.2f}')
    elif opc == 3:
        print(f'O valor em Euro {moeda} convertido para Franco e {moeda * CHF[1]:.2f}')
    elif opc == 4:
        print(f'O valor em Iene {moeda} convertido para Franco e {moeda * CHF[2]:.2f}')
    elif opc == 5:
        print(f'O valor em Rublo {moeda} convertido para Franco e {moeda * CHF[3]:.2f}')
    elif opc == 6:
        print(f'O valor em Real {moeda} convertido para Franco e {moeda * CHF[4]:.2f}')


def Euro():
    if opc == 1:
        print(f'O valor em Dolar {moeda} convertido para Euro e {moeda * EUR[0]:.2f}')
    elif opc == 2:
        print(f'O valor em Franco {moeda} convertido para Euro e {moeda * EUR[1]:.2f}')
    elif opc == 4:
        print(f'O valor em Iene {moeda} convertido para Euro e {moeda * EUR[2]:.2f}')
    elif opc == 5:
        print(f'O valor em Rublo {moeda} convertido para Euro e {moeda * EUR[3]:.2f}')
    elif opc == 6:
        print(f'O valor em Real {moeda} convertido para Euro e {moeda * EUR[4]:.2f}')


def Iene():
    if opc == 1:
        print(f'O valor em Dolar {moeda} convertido para Iene e {moeda * JPY[0]:.2f}')
    elif opc == 2:
        print(f'O valor em Franco {moeda} convertido para Iene e {moeda * JPY[1]:.2f}')
    elif opc == 3:
        print(f'O valor em Euro {moeda} convertido para Iene e {moeda * JPY[2]:.2f}')
    elif opc == 5:
        print(f'O valor em Rublo {moeda} convertido para Iene e {moeda * JPY[3]:.2f}')
    elif opc == 6:
        print(f'O valor em Real {moeda} convertido para Iene e {moeda * JPY[4]:.2f}')


def Rublo():
    if opc == 1:
        print(f'O valor em Dolar {moeda} convertido para Rublo e {moeda * RUB[0]:.2f}')
    elif opc == 2:
        print(f'O valor em Franco {moeda} convertido para Rublo e{moeda * RUB[1]:.2f}')
    elif opc == 3:
        print(f'O valor em Euro {moeda} convertido para Rublo e {moeda * RUB[2]:.2f}')
    elif opc == 4:
        print(f'O valor em Iene {moeda} convertido para Rublo e {moeda * RUB[3]:.2f}')
    elif opc == 6:
        print(f'O valor em Real {moeda} convertido para Rublo e {moeda * RUB[4]:.2f}')


def Real():
    if opc == 1:
        print(f'O valor em Dolar {moeda} convertido para Real e {moeda * REAL[0]:.2f}')
    elif opc == 2:
        print(f'O valor em Franco {moeda} convertido para Real e{moeda * REAL[1]:.2f}')
    elif opc == 3:
        print(f'O valor em Euro {moeda} convertido para Real e {moeda * REAL[2]:.2f}')
    elif opc == 4:
        print(f'O valor em Iene {moeda} convertido para Real e {moeda * REAL[3]:.2f}')
    elif opc == 5:
        print(f'O valor em Rublo {moeda} convertido para Real e {moeda * REAL[4]:.2f}')


while True:
    print('Qual moeda voce utiliza: ')
    print("=*" * 12)
    print("=*" * 3, '( 1 ) Dolar\n', end="")
    print("=*" * 3, '( 2 ) Franco\n', end="")
    print("=*" * 3, '( 3 ) Euro\n', end="")
    print("=*" * 3, '( 4 ) Iene\n', end="")
    print("=*" * 3, '( 5 ) Rublo\n', end="")
    print("=*" * 3, '( 6 ) Real\n', end="")
    print("=*" * 3, '( 7 ) Sair')
    print("=*" * 12)
    opc = int(input('Digite opcao desejada de moeda 1 a 6 : '))
    if opc == 1:
        moeda = float(input('Digite o valor em Dolar voce deseja converte: \n'))
    elif opc == 2:
        moeda = float(input('Digite o valor em Franco voce deseja converte: \n'))
    elif opc == 3:
        moeda = float(input('Digite o valor em Euro voce deseja converte: \n'))
    elif opc == 4:
        moeda = float(input('Digite o valor em Iene voce deseja converte: \n'))
    elif opc == 5:
        moeda = float(input('Digite o valor em Rublo voce deseja converte: \n'))
    elif opc == 6:
        moeda = float(input('Digite o valor em Real voce deseja converte: \n'))
    elif opc == 7:
        print("Obrigado por usar o programa, Ate a proxima")
    else:
        while opc > 7 or opc < 1:
            print('Opção invalida somente numeros inteiros de 1 a 7')
            opc = int(input('Digite opcao de moeda 1 a 6 : '))

    print('Para qual moeda voce deseja fazer intercambio: ')
    print('( 1 ) Dolar\n'
          '( 2 ) Franco\n'
          '( 3 ) Euro\n'
          '( 4 ) Iene\n'
          '( 5 ) Rublo\n'
          '( 6 ) real \n'
          '( 7 ) Todos'
          '( 8 ) Sair')

    print('Para qual voce deseja converter')
    opcao = int(input('Digite opcao de moeda para interecambia de 1 a 7 : '))
    while opcao > 8 or opcao < 1:
        print('Opção invalida somente numeros inteiros de 1 a 7')
        opcao = int(input('Digite opcao de moeda para interecambia de 1 a 7 : '))

    while opcao == opc:
        print('Não pode ser a mesma moeda')
        opcao = int(input('Digite opcao de moeda para interecambia de 1 a 7 : '))
    if opcao == 1:
        Dolar()
    elif opcao == 2:
        Franco()
    elif opcao == 3:
        Euro()
    elif opcao == 4:
        Iene()
    elif opcao == 5:
        Rublo()
    elif opcao == 6:
        Real()
    elif opcao == 7:
        Dolar()
        Franco()
        Euro()
        Iene()
        Rublo()
        Dolar()
    elif opcao == 8:
        print("Obrigado por usar o programa, Ate a proxima")
        break
