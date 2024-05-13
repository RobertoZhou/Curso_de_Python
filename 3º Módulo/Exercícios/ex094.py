geral = list()
usuario = dict()
soma = media = 0
while True:
    usuario.clear()
    usuario['nome'] = str(input('Nome: ')).title()
    while True:
        usuario['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if(usuario['sexo'] in 'MF'):
            break
        print('\033[31mERRO!\033[m Por Favor, Digite M ou F.')
    usuario['idade'] = int(input('Idade: '))
    soma += usuario['idade']
    geral.append(usuario.copy())
    while True:
        resp = str(input('Quer Continuar? [S/N] ')).upper()[0]
        if(resp in 'SN'):
            break
        print('\033[31mERRO!\033[m Responda Apenas S ou N.')
    if(resp == 'N'):
        break
print('-=' * 30)
print(f'\033[36mA)\033[m Ao Todo Temos {len(geral)} Pessoas Cadastradas.')
media = soma / len(geral)
print(f'\033[36mB)\033[m A Média De Idade É De {media :5.2f} Anos.')
print(f'\033[36mC)\033[m As Mulheres Cadastradas Foram:', end=' ')
for f in geral:
    if(f['sexo'] in 'F'):
        print(f'{f["nome"]}', end='; ')
print()
print(f'\033[36mD)\033[m Lista Das Pessoas Que Estão Acima Da Média:')
for p in geral:
    if(p['idade'] >= media):
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')
print(' <<< ENCERRADO >>>')
