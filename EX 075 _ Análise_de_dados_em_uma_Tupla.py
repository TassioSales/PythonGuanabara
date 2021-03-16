num = (int(input("Digite um numero: ")), int(input("Digite um numero: ")), int(input("Digite um numero: ")),
       int(input("Digite um numero: ")))
print(f'Voce digitou {num}')
print(f'O valor 9 apareceu{num.count(9)} vez')
if 3 in num:
    print(f'O valor 3 parece na {num.index(3) + 1}')
else:
    print("O valor 3 nao apareceu em nenhuma posição")
for n in num:
    if n % 2 == 0:
        print(f'O numeros pares digitados :{n}', end=" ")
