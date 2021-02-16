aluno = {}

aluno['Nome'] = str(input("Digite o nome do aluno: "))
aluno['Media'] = float(input(f'Digite a media do aluno {aluno["Nome"]} '))

if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situacao'] = 'Recuperação'
else:
    aluno['Situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} e igual a {v}')
