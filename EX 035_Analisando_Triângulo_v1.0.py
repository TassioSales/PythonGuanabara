print("-=-" * 20)
print("Analisado de triangulos:")
print("-=-" * 20)
r1 = float(input("Primeiro seguimento: "))
r2 = float(input("Segundo seguimento:  "))
r3 = float(input("Terceiro seguimento: "))
 
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f"Os segmentos {r1}, {r2}, {r3} PODEM FORMA TRIANGULO") 
else:
    print(f"Os segmentos {r1}, {r2}, {r3} NAO PODEM FORMA TRIANGULO")


