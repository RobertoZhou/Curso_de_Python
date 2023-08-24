valores = []
while True:
    valores.append(int(input('Digite Um Valor: ')))
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer Continuar? [S/N] '))
    if(resp in 'Nn'):
        break
print('=-' * 40)
print(f'Você Digitou {len(valores)} Elementos.')
valores.sort(reverse=True)
print(f'Os Valores Em Ordem Decrescente São {valores}')
if 5 in valores:
    print(f"O Valor 5 Faz Parte Da Lista. Ela Está Na {valores.index(5)} Posição")
else:
    print('O Valor 5 Não Foi Encontrado Na Lista')