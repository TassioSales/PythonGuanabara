soma = cont = 0
for c in range(0, 6):
    num = int(input(f"Digite o {c} valor: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"Voce informou {cont} pares  e a soma desses numeros foi {soma}") 



