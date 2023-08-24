lista = []
pares = []
impares = []
print('=-' * 40)
while True:
    valor = int(input('Digite Um Número: '))
    lista.append(valor)
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer Continuar? [S/N] ')).strip()
    if(resp in 'Nn'):
        break
for v in lista:
    if(v % 2 == 0):
        pares.append(v)
    else:
        impares.append(v)
print('=-' * 40)
print(f'A Lista Completa: {lista}')
print(f'A Lista De Pares: {pares}')
print(f'A Lista De Ímpares: {impares}')