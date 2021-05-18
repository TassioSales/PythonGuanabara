def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[0;31mErro digite uma numero inteiro valido.\33')     
        if ok:
            break
    return valor
    
        
n = leiaInt("Digite um numero:")
print(f"Voce acabou de digita o numero {n} ")
    

