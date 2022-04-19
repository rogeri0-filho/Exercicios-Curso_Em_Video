def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um valor n e retorna seu resultado.
    :param n: Valor que terá seu fatorial calculado
    :param show: Parametro opcional, caso o usuário deseje vizualizar o calculo.
    :return: O valor fatorial de um número n
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
