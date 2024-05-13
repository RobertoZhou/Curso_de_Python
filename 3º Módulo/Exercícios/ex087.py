coluna = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = coluna3 = maior2 = 0
for c in range(0, 3):
    for i in range(0, 3):
        num = int(input(f'Digite Um Valor Para [{c}, {i}]'))
        coluna[c][i] = num
        if(num % 2 == 0):
            par += num
        if(i == 2):
            coluna3 += num
        if(c == 1):
            if(i == 0):
                maior2 = num
            elif(num > maior2):
                maior2 = num
print('=-' * 40)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{coluna[c][i] :^5}]', end = ' ')
    print()
print('=-' * 40)
print(f'\033[31mA Soma Dos Valores Pares É {par}.')
print(f'\033[32mA Soma Dos Valores Da 3° Coluna É {coluna3}.')
print(f'\033[33mO Maior Valor Da 2° Linha É {maior2}.')
