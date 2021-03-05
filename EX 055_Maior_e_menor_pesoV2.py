maior = 0
menor = 0
num = int(input("Digite quantas pessoas deseja adicionar: "))
for c in range(1, num):
    peso =  float(input(f'Digite o peso da {c} pessoa:'))
    if c == 1: 
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso 
        if peso < menor:
            menor = peso
print(f"O maior peso encontrado {maior}")
print(f'O menor peso encontrado {menor}')

