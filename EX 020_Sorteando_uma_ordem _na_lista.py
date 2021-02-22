from random import shuffle
a1 = input('1ª aluno: ')
a2 = input('2ª aluno: ')
a3 = input('3º aluno: ')
a4 = input('4º aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'o aluno sorteado foi: {lista}')