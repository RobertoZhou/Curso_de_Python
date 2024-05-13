cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
        'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
        'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite Um Número Entre 0 e 20: '))
    while num not in range(0, 21):
        num = int(input('Tente Novamente. Digite Um Número Entre 0 e 20: '))
    print(f'Você Digitou o Número {cont[num]}')
    resp = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if(resp == 'N'):
        break
