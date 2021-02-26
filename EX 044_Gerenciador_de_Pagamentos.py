def avista(valor):
    valorAvista =  valor - (valor * 10 / 100)
    print("Sua compra com pagamento a avista tem um desconto de 10% ")
    print(f"Sua compra que estava no valor de {valor} vai sair por {valorAvista}")
def Debito(valor):
    debitoAvista = valor - (valor * 5 / 100)
    print("Sua compra que com pagamento no Cartão de debito tem um desconto de 5%")
    print(f"Sua compra que estava no valor de {valor} vai sair por {debitoAvista}")
def creditoAte2x(valor):
    vezes =  int(input("Digite em quantas vezes ira parcelar: 1 ou 2 vezes: "))
    if vezes == 1 or vezes == 2:
        print("Não temos desconto para compras parceladas em ate 2 vezes")
        credito2x =  valor / vezes
        print(f"Sua compra tem uma valor inicial de {valor}")
        print(f"Esse valor vai ficar parcelado em {vezes} x {credito2x}")
    else:
        print("Lembramos que para esse opção e permitido apenas dividir em ate 2 vezes")

def creditoMaior2x(valor):
    vezes =  int(input("Digite em quantas vezes ira parcelar: "))
    valorFinal = valor + (valor * 20 / 100)
    print("Para compras dividas acima de 2x temos um juros de 20%")
    print(f"Então sua compra que era de {valor}  com o juros saira por {valorFinal}")
    valorParcela = valorFinal / vezes
    print(f"O valor {valorFinal} divido em {vezes} vezes") 
    print(f"Ficara em {vezes} x {valorParcela}")

    
valorCompra = float(input("Digite o valor da sua compra: "))
print("-=-" * 20)
print("FORMAS DE PAGAMENTO")
print("-=-" * 20)
print("[ 1 ] a vista dinheiro/cheque\n"
      "[ 2 ] a vista catão debito\n"
      "[ 3 ] 2 x cartão de credito\n"
      "[ 4 ] 3 x ou mais no cartão de credito\n")
opc = int(input("Digite a opção de desejada: "))

if opc == 1:
    avista(valorCompra)
elif  opc == 2:
    Debito(valorCompra)
elif opc == 3:
   creditoAte2x(valorCompra)
elif opc == 4:
   creditoMaior2x(valorCompra) 
