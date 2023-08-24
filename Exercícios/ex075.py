num = (int(input('Digite Um Número: ')), int(input('Digite Outro Número: ')),
       int(input('Digite Mais Um Número: ')), int(input('Digite O Último Número:')))
print(f'Você Digitou Os Valores: {num}')
print(f'O Valor 9 Apareceu {num.count(9)} Vezes.')
if(3 in num):
    print(f'O Valor 3 Apareceu na {(num.index(3)) + 1}ª Posição.')
else:
    print('O Valor 3 Não Foi Digitado Em Nenhuma Posição.')
print(f'Os Valores Pares Digitados Foram', end = ' ')
for i in num:
    if(i % 2 == 0):
        print(f'{i}', end = ' ')