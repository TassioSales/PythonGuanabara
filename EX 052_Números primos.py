num = int(input("Digite um numero: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f"{c}", end = " ")
print(f"\n\33[mO numero  {num} foi divisivel em {tot} vezes")
if tot == 2:
    print("E por isso ele  e primo ")
else:
    print("E por isso ele nao e primro")