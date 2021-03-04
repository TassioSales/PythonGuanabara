primeiro = int(input("Digite o primeiro termos:"))
razão = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo, razão):
    print(f'{c}', end=' ')
print("ACABOU")