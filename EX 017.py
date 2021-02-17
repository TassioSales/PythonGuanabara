import math

cateto_op = float(input("Qual comprimento cateto oposto ? "))
cateto_ad = float(input("Qual comprimento cateto adijacente ? "))

hi = math.hypot(cateto_op, cateto_ad)

print(f'A hipotenuza vai medi {hi:.2f}')