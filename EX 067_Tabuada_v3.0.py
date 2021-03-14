while True:
    tabuada = int(input("Qual numero voce deseja ver a tabuada ?"))
    if tabuada < 0:
        break
    print("-" * 30)
    for c in range(1,11):
        print(f'{tabuada} X {c} = {tabuada * c}')
    print("-" * 30)



