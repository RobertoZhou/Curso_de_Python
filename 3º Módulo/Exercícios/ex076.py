listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
            'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34,9)
print('_' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('_' * 40)
for x in range(0, len(listagem) - 1):
    if(x % 2 == 0):
        print(f'{listagem[x]:.<25}', end = ' ')
    else:
        print(f'R${listagem[x]:>7.2f}')
print('_' * 40)