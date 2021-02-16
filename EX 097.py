def tamanhofrase (frase):
    print('~' * len(frase))
    print(frase)
    print('~' * len(frase))

tamanhofrase('Voce e muito doido')
tamanhofrase('VEC')
tamanhofrase('Queria ter sorte')

fra = str(input("Dite a frase desejada: "))
tamanhofrase(fra)