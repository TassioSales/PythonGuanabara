qtd = int(input('Digite quantas notas voce deseja adicionar: '))
nota = []
num = 1
for c in range(0, qtd):
    nota.append(float(input(f"Digite a sua nota {c + 1} nota: ")))
for item in nota:
    print(f'{num}º nota e {item}')
    num += 1
media = sum(nota) / qtd
print(f"A media dessas notas e {media}")

