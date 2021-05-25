cores = ('\33[m',
         '\33[0;40;41m',
         '\33[0;30;46m',
         '\33[0;35;43m',
         '\33[0;43;47m',);



def ajuda(com):
    titulo(f'Acessando manual de comandos \'{com}\'', 4)
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')


comando = ""
while True:
    titulo('Sistema de ajuda PYHelp', 1)
    comando = str(input('Função ou Biblioteca > '))

    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Ate Logo',1)