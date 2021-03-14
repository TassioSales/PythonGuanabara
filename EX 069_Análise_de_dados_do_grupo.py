contM = contF20 = tot18 = contF=0
while True:
    idade = (int(input("Idade: ")))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: ")).strip().upper()[0]
        if idade >= 18:
           tot18 = 1
        if sexo == "M":
            contM += 1
        if sexo ==  "F" and idade < 20:
            contF20+= 1
        if sexo == 'F':
            contF += 1
    opc = " "
    while opc not in 'SN':
        opc = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if opc == "N":
        break
print("Acabou")
print(f'Total de pessoas com mais de 18 anos {tot}')
print(f"Temos um total de {contM} homens")
print(f"Temos um total de {contF20} de mulheres com menos de 20 anos ")
print(f'Temos um total de {contF} de mulheres cadstradas')
