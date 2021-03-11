lista = list()
opc ='Ss'

while opc in "Ss":
    lista.append(float(input("Digite um numero: ")))
    opc  = str(input("Quer continuar[S/N]: "))

print(f"""A soma dos numero digitado e {sum(lista)}
Voce digitou {len(lista)} numeros
O menor numero digitado e {min(lista)}
O maior numero digitado e  {max(lista)}
A media dos numero digitados e {sum(lista) / len(lista)}""")
