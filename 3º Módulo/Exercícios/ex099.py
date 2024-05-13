from time import sleep
def maior(* valor):
    print('-=' * 30 )
    print('Analisando Os Valores Passados...')
    for i in range(0, len(valor)):
        print(valor[i], end =' ', flush = True)
        sleep(0.5)
    print(f'Foram Informados {len(valor)} Valores Ao Todo.', flush = True)
    sleep(0.5)
    print(f'O Maior Valor Informado Foi', end = ' ')
    if(len(valor) == 0):
        valor = 0
        print(valor)
    else:
        print(max(valor))
# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()