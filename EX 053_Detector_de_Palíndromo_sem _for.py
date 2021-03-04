frase = str(input("Digite uma frase: ")).upper().strip()
palavras = frase.split()
junto= "".join(palavras)
inverso = junto[::-1]
print(junto, inverso)
if inverso == junto:
    print("Temos um palindromo")
else:
    print("A frase digitada nao e um palindromo")