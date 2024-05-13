print('{:=^40}'.format(' Gerador De PA '))
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão Da PA: '))
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end = ' → ')
        termo += razao
        cont += 1
    print('Pause')
    mais = int(input('Quantos Termos Você Quer Mostrar A Mais? '))
print('\033[34mProgressão Finalizada com {} Termos Mostrados.'.format(total))