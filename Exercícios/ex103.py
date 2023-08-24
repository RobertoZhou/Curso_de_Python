def ficha(jogador='<desconhecido>', gol=0):
    print(f'O jogador {jogador}, fez {gol} gols.')
n = input('Jogador: ').strip()
g = input('Gols: ')
if(g.isnumeric()):
    g = int(g)
else:
    g = 0
if(n == ''):
    ficha(gol=g)
else:
    ficha(n, g)
    