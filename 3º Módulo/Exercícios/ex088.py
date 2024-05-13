from random import randint
from time import sleep
numeros = list()
print('_' * 40)
print(f'{"JOGO NA MEGA SENA" :^40}')
print('_' * 40)
quantidade = int(input('Quantos Jogos Você Quer Que Eu Sorteie? '))
print('{0} SORTEANDO {1} JOGOS {0}'.format('=-' * 5, quantidade))
for i in range(1, quantidade + 1):
    for x in range(0, 6):
        while True:
            n = randint(1, 60 + 1)
            if n not in numeros:
                numeros.append(n)
                break
    sleep(0.5)
    numeros.sort()
    print(f'Jogo {i} {(numeros)}')
    numeros.clear()
print(f'{" < BOA SORTE > " :=^40}')
