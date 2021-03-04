from datetime import date
anoAtual = date.today().year

numPessoas =  int(input("Quantas datas voce deseja adicionar ? "))
pessoas = []
for c in range (0, numPessoas):
    contmaior = 0
    contmenor = 0
    pessoas.append(int(input((f'Em que ano a {c+1} pessoa nasceu ?'))))
    for data in pessoas:
        idade = anoAtual - data
        if idade <= 17:
            contmenor += 1
        elif idade > 17:
            contmaior += 1
print(pessoas)
print(f"""
No total temos {contmaior} pessoas maires de idade\n
e temos {contmenor} pessoas menores de idade
""")
