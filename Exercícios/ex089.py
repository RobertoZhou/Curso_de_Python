aluno = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno.append([nome, [nota1, nota2]])
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja Contianur? [S/N] ')).upper()
    if continuar == 'N':
        break
print('=-' * 40)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('_' * 40)
for c, i in enumerate(aluno):
    print(f'{c :<4}{i[0] :<10}{((i[1][0] + i [1][1]) / 2) :>8.1f}')
print('_' * 40)
while True:
    mostrar = int(input('Mostrar Notas De Qual Aluno? (999 Interrompe): '))
    if(mostrar == 999):
        print('FINALIZANDO...')
        break
    if(mostrar <= len(aluno) - 1):
        print(f'Notas De {aluno[mostrar][0]} são {aluno[mostrar][1]}')
print('<<<< VOLTE - SEMPRE >>>>')