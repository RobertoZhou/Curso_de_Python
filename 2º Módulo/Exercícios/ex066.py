n = cont = soma = 0
while True:
    n = int(input('Digite Um Valor (999 Para Parar): '))
    if(n == 999):
        break
    cont += 1
    soma += n
print(f'A Soma Dos {cont} Valores Foi {soma}!')