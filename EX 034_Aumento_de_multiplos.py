salario = float(input("Digite o salario do funcionario R$ "))
if salario <= 1250:
    novosalario = salario + (salario * 15 / 100)
    print(f"O salario do funcionario que era R$ {salario} depois do aumento de 15% ficara {novosalario}")
elif salario > 1250:
    novosalario = salario + (salario * 10 / 100)
    print(f"O salario do funcionario que era R$ {salario} depois do aumento de 10% ficara {novosalario}")
else:
    print("Valor invalido")