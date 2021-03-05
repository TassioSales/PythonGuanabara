somaidade = 0
mediaidade = 0
maioridadedehomem = 0
nomedovelho = 0 
totmulher20 = 0
for c in range (0,4):
    nome = str(input("Nome: ")).strip()
    idade= int(input('Digite sua idade: '))
    sexo = str(input("Sexo[M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadedehomem = idade 
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadedehomem:
        maioridadedehomem = idade 
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1


mediaidade = somaidade / 4
print(f'A media de idade e {mediaidade} anos ')
print(f'O homem mais velho tem {maioridadedehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')


