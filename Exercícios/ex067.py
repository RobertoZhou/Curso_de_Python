while True:
    print('-' * 45)
    tabuada = int(input('Quer Ver A Tabuada De Qual Valor? '))
    print('-' * 45)
    if(tabuada < 0):
        break
    for x in range(1, 11):
        print(f'{tabuada} X {x} = {tabuada * x}')
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')