registro = dict()
usuario = list()
gols = list()
while True:
    registro.clear()
    gols.clear()
    registro['nome'] = str(input('Nome Do Jogador: ')).title()
    registro['gols'] = int(input(f'Quantas Partidas {registro["nome"]} Jogou? '))
    for g in range(0, registro['gols']):
        gols.append(int(input(f'    Quantos Gols Na {g+1}° Partida? ')))
    registro['gols'] = gols[:]
    registro['total'] = sum(registro['gols'])
    usuario.append(registro.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).upper()[0]
        if(resp in 'SN'):
            break
        print('ERRO! Responda Apenas S ou N.')
    if(resp == 'N'):
        break
print('-=' * 30)
print('Cod  ', end=' ')
for i in registro.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(usuario):
    print(f'{k:<6}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 30)
while True:
    resp = int(input('Mostrar Os Dados De Qual Jogador? (999 Para Parar) '))
    if(resp == 999):
        break
    elif(resp >= len(usuario)):
        print(f'ERRO! Não Existe Jogador Com Codigo {resp}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {usuario[resp]["nome"].upper()}:')
        for i in range(0, len(usuario[resp]['gols'])):
            print(f'    No {i+1}° Jogo, Fez {usuario[resp]["gols"][i]} Gols.')
        print('-' * 30)
print('<<< VOLTE SEMPRE >>>')
