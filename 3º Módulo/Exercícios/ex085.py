num = [[], []]
for i in range(1, 8):
    valor = int(input(f'Digite O {i}ª Valor: '))
    if(valor % 2 == 0):
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=-' * 40)
num[0].sort()
num[1].sort()
print(f'\033[32mOs Valores Pares Digitados Foram: {num[0]}')
print(f'\033[33mOs Valores Ímpares Digitados Foram: {num[1]}')