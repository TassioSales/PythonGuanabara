from datetime import date

anoAtual = date.today().year

idade = int(input("Digite o ano do ser nacscimento: "))

idadeAtual =  anoAtual - idade

if idadeAtual <= 9:
    print(f"Voce tem {idadeAtual} anos")
    print("Classificação: MIRIM")
elif idadeAtual <= 14:
    print(f"Voce tem {idadeAtual} anos")
    print("Classificação: INFANTIL")
elif idadeAtual <= 19:
    print(f"Voce tem {idadeAtual} anos")
    print("Classificação: JÚNIOR")
elif idadeAtual <= 25:
    print(f"Voce tem {idadeAtual} anos")
    print("Classificação: SÊNIOR")
else:
    print(f"Voce tem {idadeAtual:.2f} anos")
    print("Classificação: MASTER")
