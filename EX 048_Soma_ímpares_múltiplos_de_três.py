soma = 0
cont = 0
for c in range (0,501, 2):
    if c % 3 == 0:
       cont += 1
       soma += c 
print(f"A soma de todos os valores e {soma} ")
print(f"A quantidade de numeros somados foram {cont}")