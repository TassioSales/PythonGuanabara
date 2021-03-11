primeiro = int(input("Digite o primeiro termos:"))
razao = int(input("Razão: "))
termo = primeiro
cont = 1

while cont <= 10:
    print(f"{termo} ->", end=" ")
    termo += razao
    cont += 1
print("FIM")