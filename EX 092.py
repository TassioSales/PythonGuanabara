from datetime import datetime
trabalhador = dict()


trabalhador['Nome'] = str(input("Digite seu nome : "))
nasc = int(input("Digite o ano de nascimento :"))
trabalhador['idade'] = datetime.now().year - nasc
trabalhador['CTPS'] = int(input('Digite o numero da CTPS (0 não tem) : '))
if trabalhador['CTPS'] != 0:
    trabalhador['contratação'] = int(input("Ano de contração : "))
    trabalhador['Salario'] = float(input("Salario R$"))
    trabalhador['Aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - datetime.now().year)

print('X' * 25)

for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
