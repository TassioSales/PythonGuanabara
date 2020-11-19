roupa = []
valor = []


def adicionar():
    roupa.append(input('Digite qual tipo de roupa : '))
    valor.append(float(input("Digite o valor")))


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
          '( 7 ) Outro tipo de desconto\n'
          '( 8 ) Cancelar compra\n')
          


def menuprincipla():
    print('MENU\n'
          '(1)ADICIONAR\n'
          '(2)EXCLUIR\n'
          '(3)MODIFICAR\n'
          '(4)DESCONTO\n'
          '(5)MOSTRA ITENS\n'
          '(6)VALOR TOTAL\n')


def menubancos():
    print('INFORME AO CLIENTE OS BANCOS')
    print('( 1 ) BANCO BRASIL\n'
          '( 2 ) CAIXA ECONOMIDA\n'
          '( 3 ) ITAU\n')


def valor_tot():
    while True:
        valorTotal = sum(valor)
        for c in range(0, len(roupa)):
            print(f'COD : \033[31m{c}\033[m TIPO \033[36m{roupa[c]}\033[m  VALOR R$ \033[35m{valor[c]}\033[m\n')

        menuformaspagemento()
        opcao = int(input('Digite a opção desejada: '))

        if opcao == 1:
            print(f'O valor total dos produtos deu: R${valorTotal}')
            tot_desc = 15
            desc = valorTotal - (valorTotal * tot_desc / 100)
            print(f'Para pagamentos avista voce tem {tot_desc}% de desconto')
            print(f"O valor Total R${valorTotal} com desconto {tot_desc}% ficou por R${desc}")
            dinheiroCliente = float(input("Qual valor pago: "))
            if dinheiroCliente == desc:
                print('Obrigado pela preferencia')
                valor.clear()
                roupa.clear()
                break
            elif dinheiroCliente > desc:
                troco = dinheiroCliente - desc
                print(f"Retorne o troco de R${troco:.2f}")
                print(f'Obrigado pela prefencia:')
                valor.clear()
                roupa.clear()
                break
            elif dinheiroCliente < desc:
                print('Valor menor doque o necessario')
                print(f'Ainda falta {desc - dinheiroCliente}')
                print('Restorne ao menu')
        elif opcao == 2:
            print(f'O valor total dos produtos deu: R${valorTotal}')
            cartaoDebito = 10
            desc = valorTotal - (valorTotal * cartaoDebito / 100)
            print(f'Para pagamentos Debito voce tem {cartaoDebito}% de desconto')
            print(f"O valor Total R${valorTotal} com desconto {cartaoDebito} ficou por {desc}")
            break
        elif opcao == 3:
            print(f'O valor total dos produtos deu: R${valorTotal}')
            parcelas = int(input('Digite em quantas vezes voce quer dividir : '))
            if parcelas == 1 or parcelas == 2:
                cartaoC_1e2 = 8
                desc = valorTotal - (valorTotal * cartaoC_1e2 / 100)
                print(f'Para pagamentos credito em 1 ou 2 vezes voce tem {cartaoC_1e2}% de desconto')
                print(f"O valor Total R${valorTotal} com desconto {cartaoC_1e2} ficou por {desc}")
                print('De o cupom para o cliente')
                break
            elif parcelas >= 3 or parcelas <= 12:
                cartaoC_3a12 = 5
                desc = valorTotal - (valorTotal * cartaoC_3a12 / 100)
                print(f'Para pagamentos credito em 3 ate 12 vezes voce tem {cartaoC_3a12}% de desconto')
                print(f"O valor Total R${valorTotal} com desconto {cartaoC_3a12} ficou por {desc}")
                print('De o cupom para o cliente')
                break
            elif parcelas > 12:
                cartaoC_maiorq12 = 7
                desc = valorTotal + (valorTotal * cartaoC_maiorq12 / 100)
                print(f'Para pagamentos credito maior que 12 vezes  voce tem um adicional de {cartaoC_maiorq12}%')
                print(f"O valor Total R${valorTotal} com desconto {cartaoC_maiorq12} ficou por {desc}")
                print(f'De o cumpom para o cliente')
                break
        elif opcao == 4:
            print(f'O valor total dos produtos deu: R${valorTotal}')
            print('informe para o cliente que para cheque nao tem desconto: ')
            op = str(input('O cliente ainda quer pagar em cheque S/N?'))
            if op == 'S':
                continue
            elif op == "N":
                break
            chequeAssinado = str(input('Verifique se o cheque esta assinado :')).upper().strip()
            chequeValor = str(input("Verifique se o valor corresponde ")).upper().strip()
            if chequeAssinado == "S" and chequeValor == "S":
                print("Obrigado pela compra")
                valor.clear()
                roupa.clear()
                break
            elif chequeAssinado == "N":
                print("Peça para o cliente Assinar o cheque")
                chequeAssinado = str(input('O Cheque foi assinado ? :')).upper().strip()
                if chequeAssinado == "S":
                    print("Obrigado pela preferencia")
                    valor.clear()
                    roupa.clear()
                    break
                else:
                    print('Troque a forma de pagamanto ou cancele a compra : ')
                    break
        elif opcao == 5:
            menubancos()
            bancos = int(input('Qual banco de preferencia: '))
            if bancos == 1:
                print('BANCO DO BRASIL')
                print('informe a conta e agencia para o cliente :')
                print('Conta: XXXXX-XX Agencia: XXXXXX-XXX')
                print('Peça o comprovante de pagamento para o cliente')
                print('Verifique se pagamente foi realizado:')
                comprovante = input("Esta tudo correto S/N").upper().strip()
                if comprovante == "S":
                    print("Obrigado pela prefencia")
                    valor.clear()
                    roupa.clear()
                    break
                elif comprovante == "N":
                    print('Peça para o cliente verificar:')
                    print("Ou alterar a forma de pagamento:")
                else:
                    print('Opção invalida')
            elif bancos == 2:
                print('CAIXA ECONOMICA')
                print('informe a conta e agencia para o cliente :')
                print('Conta: XXXXX-XX Agencia: XXXXXX-XXX')
                print('Peça o comprovante de pagamento para o cliente')
                print('Verifique se pagamente foi realizado:')
                comprovante = input("Esta tudo dentro dos correto S/N").upper().strip()
                if comprovante == "S":
                    print("Obrigado pela prefencia")
                    valor.clear()
                    roupa.clear()
                    break
                elif comprovante == "N":
                    print('Peça para o cliente verificar:')
                    print("Ou alterar a forma de pagamento:")
                else:
                    print('Opção invalida')
            elif bancos == 3:
                print('ITAU')
                print('informe a conta e agencia para o cliente :')
                print('Conta: XXXXX-XX Agencia: XXXXXX-XXX')
                print('Peça o comprovante de pagamento para o cliente')
                print('Verifique se pagamente foi realizado:')
                comprovante = input("Esta tudo dentro dos correto S/N").upper().strip()
                if comprovante == "S":
                    print("Obrigado pela prefencia")
                    valor.clear()
                    roupa.clear()
                    break
                elif comprovante == "N":
                    print('Peça para o cliente verificar:')
                    print("Ou alterar a forma de pagamento:")
                else:
                    print('Opção invalida')
            else:
                print('Opção invalida')
                print('Retorne ao MENU')


while True:

    menuprincipla()

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
        valor_tot()
    else:
        print("OPÇÃO INVALIDA")
        continue
