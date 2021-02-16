pessoas = dict()
cadpessoas = list()
soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome : '))
    while True:
        pessoas['Sexo'] = str(input('Sexo: ')).upper()[0]
        if pessoas['Sexo'] in "MF":
            break
        print(" Por favor, Responda apenas M ou F")
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    cadpessoas.append(pessoas.copy())
    while True:
        resp = str(input('Quer Continuar ? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print("ERRO!, Responda apenas S ou N")
    if resp == 'N':
        break
print(f'A o todo tesmo {len(cadpessoas)} pessoas cadastrasdas')
media = soma / len(cadpessoas)
print(f'A media de idade e de {media:5.2f} anos')
print(f'A soma das idade e {soma}')
print(f'As muleres cadastradas foram', end=' ')
for p in cadpessoas:
    if p['Sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('Lista de pessoas acima da media')
for p in cadpessoas:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}:', end=' ')
        print()
print('ENCERRADO')



