primeiro = int(input("Digite o primeiro termos:"))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} ->", end=" ")
        termo += razao
        cont += 1
    print("PAUSA ")
    mais = int(input("Quanto temos voce quer mostra a mais ?"))
print(f"Progreção com {total} termos mostrados")