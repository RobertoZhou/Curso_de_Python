print('{:=^40}'.format(' Gerador De PA '))
termo1 = int(input('Primeiro Termo: '))
razao = int(input('Razão Da PA: '))
final = int(input('Informe O Limite Do PA: '))
cont = 1

while(cont <= final):
    print('\033[32m{} → '.format(termo1), end = '')
    termo1 += razao
    cont += 1
print('\033[31mFinal')