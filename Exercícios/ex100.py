from random import randint
numeros = list()
def sorteio():
    print(f'Sortendo 5 Valores Da Lista:', end=' ')
    for i in range(0, 5):
        numeros.append(randint(1, 10))
        print(numeros[i], end =' ')
    print('PRONTO!')

def somaPar():
    par = 0
    for i in numeros:
        if i % 2 == 0:
            par += i
    print(f'Somando Os Valores Pares De {numeros}, Temos {par}.')
sorteio()
somaPar()