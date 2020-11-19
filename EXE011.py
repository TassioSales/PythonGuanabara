def tinta():
    print(f'Voce vai gasta um total de {area / 2} litros de tinta para pintar a parede: ')


largura = float(input('Digite a Largura : '))
altura = float(input("Digite a Altura :"))
area = largura * altura
print(f"A parede de largura {largura} e altura {altura} da uma parede com uma area de {area}m²")

tinta()
