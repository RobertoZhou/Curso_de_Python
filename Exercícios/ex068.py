from random import randint
cont = 0
print('-=' * 20)
print('{:^40}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
while True:
    print('-=' * 20)
    computador = randint(0, 10)
    jogador = int(input('Diga Um Valor: '))
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    print('_' * 40)
    print(f'Você Jogou {jogador} e o Computador {computador}. Total de {total}', end=' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    print('_' * 40)
    if(tipo == 'P'):
        if(total % 2 == 0):
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif(tipo == 'I'):
        if(total % 2 == 1):
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
print(f'GAME OVER! Você Venceu {cont} Vezes')
