print('=' * 30)
print('{:^30}'.format("BANCO IOLO"))
print('=' * 30)

valor = int(input("Que valor você que sacar: "))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'Total {totced} cedulas d R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 1:
            ced = 1
        totced = 0
        if total == 0:
            break
    

