roupa = []
valor = []
valorTotal = sum(valor)


def adicionar():
    roupa.append(input('Digite qual tipo de roupa : '))
    valor.append(float(input("Digite o valor : ")))


def excluir():
    global c
    for c in range(0, len(roupa)):
        print(f'COD : \033[31m{c}\033[m TIPO \033[36m{roupa[c]}\033[m  VALOR R$ \033[35m{valor[c]}\033[m\n')
    opc = int(input("Qual vc deseja expluir ?"))
    while c != opc:
        print("opcão invalida")
        opc = int(input("Qual vc deseja expluir ?"))
    print(f"Voce escolheu a {opc} que e uma {roupa[c]}")
    decisao = str(input('Tem ceteza disso S/N : ')).upper().strip()
    if decisao == "S":
        del (roupa[opc])
        del (valor[opc])
    elif decisao == "N":
        print("Ok Voltando para o menu")
    else:
        print("opção invalida")
        print("Retornando ao MENU")


def modificar():
    global c
    for c in range(0, len(roupa)):
        print(f'COD : \033[31m{c}\033[m TIPO \033[36m{roupa[c]}\033[m  VALOR R$ \033[35m{valor[c]}\033[m\n')
    mod = int(input('Qual opçao vc deseja modificar:'))
    print(c)
    print(mod)
    while mod != c:
        print("opcão invalida")
        mod = int(input("Qual vc deseja modificar ?"))
    print(f"Voce escolheu a {mod} que e uma {roupa[c]}")
    decisao = str(input('Tem ceteza disso S/N : ')).upper().strip()
    if decisao == "S":
        roupa[mod] = input("Digite qual tipo de roupa:  ")
        valor[mod] = float(input("Digite o valor para modigficado :"))
    elif decisao == "N":
        print("Ok Voltando para o menu")
    else:
        print("opção invalida")
        print("Retornando ao MENU")


def desconto():
    for c in range(0, len(roupa)):
        print(f'COD : \033[31m{c}\033[m TIPO \033[36m{roupa[c]}\033[m  VALOR R$ \033[35m{valor[c]}\033[m\n')
    print(f'O valor total dos produtos deu: R${sum(valor)}')
    desc = float(input('Quantos % voce quer da de desconto'))
    totalComDesconto = sum(valor) - (sum(valor) * desc / 100)
    print(f'O total a ser pago e R$ {totalComDesconto}')


def mostra():
    for c in range(0, len(roupa)):
        print(f'COD : \033[31m{c}\033[m TIPO \033[36m{roupa[c]}\033[m  VALOR R$ \033[35m{valor[c]}\033[m\n')


def menuformaspagemento():
    print('FORMAS DE PAGAMENTO')
    print('( 1 ) Dinheiro:\n'
          '( 2 ) Cartao Debito:\n'
          '( 3 ) Credito:\n'
          '( 4 ) Cheque: \n'
          '( 5 ) Tranferecia Bancaria: \n'
          '( 6 ) Outro tipo de desconto\n'
          '( 8 ) Cancelar compra\n')


def menuprincipal():
    print('MENU\n'
          '(1)ADICIONAR\n'
          '(2)EXCLUIR\n'
          '(3)MODIFICAR\n'
          '(4)DESCONTO\n'
          '(5)MOSTRA ITENS\n'
          '(6)FINALIZAR COMPRA\n')


def menubancos():
    print('INFORME AO CLIENTE OS BANCOS')
    print('( 1 ) BANCO BRASIL\n'
          '( 2 ) CAIXA ECONOMIDA\n'
          '( 3 ) ITAU\n')


def finalizarcompra():
    menuformaspagemento()
    opc = int(input('Digite a opção desejada: '))

    def dinheiro():
        valortotal = sum(valor)
        print(valortotal)
        tot_desc = 15
        print(f'Sua compra deu um valor de R${valortotal}')
        valortotal = valortotal - (valortotal * tot_desc / 100)
        print(f'Com desconto de preço avista de 15% a compra ficara por {valortotal}')
        valorPago = float(input('Qual valor recebido para pagamento '))
        troco = valorPago - valortotal
        if valorPago > valortotal:
            print(f'Devolva para o cliente de troco o valor de R$ {troco}')
            print("Obrigado pela preferecia volte sempre:")
            valor.clear()
            roupa.clear()
        elif valorPago == valorTotal:
            print("Obrigado pela preferecia volte sempre:")
            valor.clear()
            roupa.clear()
        while valorPago < valortotal:
            continue



    if opc == 1:
        dinheiro()


while True:
    menuprincipal()
    opcao = int(input('Qual opção desejada: '))

    if opcao == 1:
        adicionar()
    elif opcao == 2:
        excluir()
    elif opcao == 3:
        modificar()
    elif opcao == 4:
        desconto()
    elif opcao == 5:
        mostra()
    elif opcao == 6:
        finalizarcompra()
    else:
        print("OPÇÃO INVALIDA")
        continue
