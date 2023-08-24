n = cont = soma = 0
while n != 999:
    n = int(input('Digite Um Número [ 999 Para Parar ]: '))
    if(n != 999):
        soma += n
        cont += 1
print('Você Digitou {} Números e a soma entre eles foi {}.'.format(cont, soma))
