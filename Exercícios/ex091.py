from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
              'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = list()
print('\033[33mValores Sorteados: \033[m')
sleep(0.5)
for k, v in jogadores.items():
    print(f'    O {k} Tirou {v}')
    sleep(0.5)
print('\033[32mRanking Dos Jogadores:\033[m')
sleep(0.5)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i+1}° Lugar: {v[0]} Com {v[1]}.')
    sleep(1)
