from datetime import date
anoAtual = date.today().year

anoNascimento = int(input("Digite o ano do seu nascimento: "))

idade = anoAtual - anoNascimento

if idade == 18:
    print("Parabens voce esta na idade para se alistar")
    print(f"Você ja tem {idade} anos")
    print("Se apresente a junta militar mais proxima de você")
elif idade < 18:
    print("Você ainda não atingiu a idade adequeda para se alistar")
    print(f"Você tem apenas {idade} anos")
    print(f'Aguarde mais {18 - idade} anos')
elif idade > 18:
    print('Você esta um pouco atrazado para se alistar')
    print(f"Você tem {idade} anos")
    print('Procure a junta militar para resolver sua situação')


