valores = []
print('=-' * 40)
for v in range(0, 5):
    valores.append(int(input(f'Digite Um Valor Para A Posição {v}: ')))

#Maior E Menor Valor:
maior = max(valores)
menor = min(valores)

print('=-' * 40)
print(f'Você Digitou Os Valores: {valores}')
print(f'O Maior Valor Digitado Foi {maior}. Nas Posições', end=' ')
for i, v in enumerate(valores):
    if(v == maior):
        print(f'{i}...', end = ' ')
print(f'\nO Menor Valor Digitado Foi {menor}. Nas Posições', end = ' ')
for i, v in enumerate(valores):
    if(v == menor):
        print(f'{i}...', end = ' ')