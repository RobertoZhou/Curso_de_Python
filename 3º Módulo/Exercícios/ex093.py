jogador = dict()
jogador['nome'] = str(input('Nome Do Jogador: ')).title()
gols = list()
tot = int(input(f'Quantas Partidas {jogador["nome"]} Jogou:'))
for p in range(0, tot):
    gols.append(int(input(f'Quantos Gols Na {p}° Partida: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O Campo {k} Tem Valor {v}')
print('-=' * 30)
print(f'O Jogador {jogador["nome"]} Jogou {len(jogador["gols"])} Partidas:')
for i, v in enumerate(jogador['gols']):
    print(f'    =>  Na Partida {i}, Fez {v} Gols.')
print(f'Foi Um Total De {jogador["total"]} Gols.')