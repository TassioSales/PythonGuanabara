emprestimo = float(input("Digite o valor do emprestimo: "))
renda =  float(input("Digite o seu salario: "))
anos = float(input("Digite em quantos anos você vai pagar: "))
parcelas = anos * 12
prestação = emprestimo / parcelas
minimo  = renda * 30 /100 
print(f"Para pagar um empretimo de R${emprestimo:.2f} em {anos:.0f} anos ")
print(f"Tem que pagar {parcelas:.0f} X {prestação:.2f}")
print(f"E a parcela minima e {parcelas:.0f} X {minimo:.2f}")
if renda <= minimo:
    print("PARABENS SEU EMPRESTIMO FOI AUTORIZADO")
else:
    print("INFELIZMENTE NAO PODEMOS AUTORIZAR SEU EMPRESTIMO NESSE MOMENTO")
    print("Salario abaixo dos 30% autorizado")