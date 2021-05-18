def factorial(n , show = False):
    """
    -> Calcula o fatorial de um numero
    :param n: O numero a ser calculado
    :param show: (optional) Mostra ou não a conta .
    :return: O valor do fatorial de um numero n.
    """
    
    f = 1
    for c in range(n, 0, -1):
        print(f'{c}', end=' ')
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#print(factorial(10, show = True))

help(factorial)
