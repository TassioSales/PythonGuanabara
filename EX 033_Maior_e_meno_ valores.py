num1 = float(input("Primeiro numero: "))
num2 = float(input("Segundo numero: "))
num3 = float(input("Terceiro numero: "))
#verificando quem e menor
menor =  num1
if num2 < num1 and num2 < num3:
    menor = num2
elif num3 < num1 and num3 < num2:
    menor = num3 
print(f"O menor valor digitado foi {menor}")
maior =  num1
if num2 > num1 and num2 > num3:
    maior = num2
elif  num3 > num1 and num3 > num2:
    maior = num3 
print(f"O maior valor digitado foi {maior}")