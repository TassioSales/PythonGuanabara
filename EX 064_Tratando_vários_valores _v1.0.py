soma = cont = 0
num = float(input("Digite um numero e [999] para PARAR: "))
while num != 999:
    soma += num
    cont += 1
    num = float(input("Digite um numero e [999] para PARAR: "))
print(f"Voce digitou {cont} numeros e a soma e {soma}")