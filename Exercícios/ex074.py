from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10), randint(1, 10))
print(f'Os Valores Sorteados Foram:', end = ' ')
for x in num:
    print(f'{x}', end = ' ')
print(f'\nO Maior Valor Sorteador Foi: {max(num)}')
print(f'O Menor Valor Sorteado Foi: {min(num)}')