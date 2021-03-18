listanum = []

for c in range(0,5):
    listanum.append(int(input(f'Digite um numero na posição {c}: ')))

print(f"O maior numero digitado foi: {max(listanum)} nas posiçôes: ", end = '')
for i, v in enumerate(listanum):
    if v == max(listanum):
        print(f'{i}....')
print(f'O menor nuemro digitado foi: {min(listanum)} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == min(listanum):
        print(f'{i}....')


