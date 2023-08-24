resp = ''
cont = total = maior = menor = 0
while resp in 'S':
    n = int(input('Digite Um Número: '))
    cont += 1
    total += n
    if(menor == 0 and maior == 0):
        maior = menor = n
    else:
        if(n > maior):
          maior = n
        if(n < menor):
            menor = n
    resp = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]
print('Você Digitou {} Números E A Média foi {}'.format(cont, total / cont))
print('O Maior Valor Foi {} E O Menor foi {}'.format(maior, menor))
