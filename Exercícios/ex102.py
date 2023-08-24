def fatorial(num, show=False):
    """
    -> Calcula O Fatorial De Um Número.
    :param num: O número a ser calculado.
    :param show: (Opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if(show == True):
            if(i > 1):
                print(f'{i} X', end=' ')
            elif(i == 1):
                print(f'{i} =', end= ' ')
    return f


# Programa Principal
print(fatorial(5))
