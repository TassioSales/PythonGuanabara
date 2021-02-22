notas = []
quantidade = int(input("Quantas notas deseja adicionar:"))
for c in range(0, quantidade):
    notas.append(float(input(f'Digite a nota {c+1}:')))
soma = sum(notas)
print(f'A soma total das notas e {soma}')
print(f'A nota media desse aluno e {soma / quantidade}')


