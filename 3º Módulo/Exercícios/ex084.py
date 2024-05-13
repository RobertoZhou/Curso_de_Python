princ = list()
temp = list()
maior = menor = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    temp.append(nome)
    temp.append(peso)
    if maior and menor == 0:
        maior = menor = peso
    else:
        if(peso > maior):
            maior = peso
        if(peso < menor):
            menor = peso
    princ.append(temp[:])
    temp.clear()
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer Continuar? [S/N] '))
    if(continuar.upper() == 'N'):
        break
print('=-' * 40)
print(f'Ao Todo Você Cadastrou {len(princ)} Pessoas')
print(f'O Maior Peso Foi De {maior :.1f} KG. Peso De', end=' ')
for p in princ:
    if(p[1] == maior):
        print(f'[{p[0]}]', end = ' ')
print(f'\nO Menor Peso Foi De {menor :.1f} KG. Peso De', end=' ')
for p in princ:
    if(p[1] == menor):
        print(f'[{p[0]}]', end = ' ')
