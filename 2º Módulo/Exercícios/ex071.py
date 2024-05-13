print('=\033[34m' * 40)
print('{:^40}'.format('BANCO CEV'))
print('=' * 40, '\033[m')
valor = int(input('Qual Valor Você Quer Sacar? R$'))
ced = 50
totalCed = 0
while True:
    if(valor >= ced):
        valor -= ced
        totalCed += 1
    else:
        if(totalCed > 0):
            print(f'Total de {totalCed} Cédulas de R${ced},00')
            totalCed = 0
        elif(ced == 50):
            ced = 20
        elif(ced == 20):
            ced = 10
        elif(ced == 10):
            ced = 1
        if(valor == 0):
            break
print('=' * 40)
print('Volte Sempre Ao Banco CEV! Tenha Um Bom Dia')