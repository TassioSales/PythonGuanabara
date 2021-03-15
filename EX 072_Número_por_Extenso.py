
numerosPorExtenso = ('Zero','Um', 'Dois','Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Deis', 'Onze', 'Doze', 'Treze', 'Catorze','Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove','Vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20 para ver por extenso: '))

    if 0 <= num <= 20:
        break
    print('Tente novamente', end = " ")

print(f"O numero digitado foi {num} ele por extenso e {numerosPorExtenso[num]}")