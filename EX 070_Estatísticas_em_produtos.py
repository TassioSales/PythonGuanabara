total= totmil = menor = cont= 0
barato= " "

while True:
    produto = str(input("nome do produto: "))
    preco = float(input("preco R$ "))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato == produto
        
    resp = " "

    while resp not in "SN":
        resp = str(input("Quer continuar ? [S/N]")).strip().upper()[0]
    if resp == "N":
        break

print("{:^40}".format("FIM DO PROGRAMA"))
print(f"O total da compra foi {total:.2f}")
print(f'voce comprou {totmil} produtos acima de 1000 reais')
print(f"o produto mais barato custa {menor:.2f}")
