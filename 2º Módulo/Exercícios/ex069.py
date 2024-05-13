print('\033[32m_' * 40)
print('{:^40}'.format('CADASTRE UMA PESSOA'))
print('_' * 40, '\033[m')
maior18 = homens = mulher_20 = 0
while True:
    while True:
        idade = input('Idade: ')
        idadeVerif = idade.isdigit()
        if(idadeVerif == True):
            idade = int(idade)
            break
    if(idade >= 18):
        maior18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if(sexo == 'M'):
        homens += 1
    if(sexo == 'F') and (idade < 20):
        mulher_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if(continuar == 'N'):
        break
print('{:=^40}'.format(' FIM DO PROGRAMA '))
print(f'Total de Pessoas Com Mais de 18 Ano: {maior18}')
print(f'Ao Todo Temos {homens} Homens Cadastrados.')
print(f'E Temos {mulher_20} Mulheres Com Menos de 20 Anos.')