from time import sleep
def contagem(i, f, p):
    if(p == 0):
        p = 1
    print('=-' * 20)
    print(f'Contagem De {i} Até {f} De {abs(p)} Em {abs(p)}:')
    sleep(2.5)
    p = abs(p)
    if(i < f):
        f = f + 1
    elif(i > f):
        p = -p
        f = f - 1
    for i in range(i, f, p):
        print(i, end=' ', flush = True)
        sleep(0.5)
    print('FIM!')

contagem(1, 10, 1)
contagem(10, 0, 2)
print('=-' * 20)
print('Agora É Sua Vez De Personalizar A Contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
