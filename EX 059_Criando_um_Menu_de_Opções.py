def somar (n1, n2):
    soma = n1 + n2
    print(f"A soma dos numeros {n1} e {n2} = {soma}")

def subtracao(n1, n2):
    subtracao = n1 - n2
    print(f"A subtracao dos numeros {n1} e {n2} = {subtracao}")

def multiplicacao(n1, n2):
    multiplicacao =  n1 * n2 
    print(f"A multiplicação  dos numeros {n1} e {n2} = {multiplicacao}")

  
def maior(n1, n2):
    maior = n1
    if n2 > n1:
        maior = n2
    print(f"O maior numero digitado foi {maior}")
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor : "))
while True:
    print("""
    [ 1 ] somar
    [ 2 ] subtrair
    [ 3 ] multiplicação
    [ 4 ] Novos numeros
    [ 5 ] Maior
    [ 6 ] Sair
""")
    opt = int(input("Digite sua opção: "))
    if opt == 1:
        somar(num1, num2)
    elif opt == 2:
        subtracao(num1, num2)
    elif opt == 3:
        multiplicacao(num1, num2) 
    elif opt == 4:
         num1 = float(input("Digite o primeiro numero: "))
         num2 = float(input("Digite o segundo numero: "))
         print(f"Os novos numeros digitatos foram {num1} e {num2}")
         continue
    elif opt == 5:
        maior(num1, num2)
    elif  opt == 6:
        break
    else:
        print("Opção invalida")
        continue

()