distancia = float(input("Digite a distancia da viagem : "))
print(f"Voce esta prestes a começar uma viagem de {distancia}km")
if distancia <= 200.0:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'E o preço da sua passagem será de R${preco:.2f}')  