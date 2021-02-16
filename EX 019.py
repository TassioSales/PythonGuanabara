from random import choice
alunos = []
a1 = input('primeiro aluno: ')
a2 = input('segundo aluno: ')
a3 = input('teceiro aluno: ')
a4 = input('quarto aluno: ')
alunos = [a1, a2, a3, a4]
print(f'o aluno escolhido foi {choice(alunos)} ')
