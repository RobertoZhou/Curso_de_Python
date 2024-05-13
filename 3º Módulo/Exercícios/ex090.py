aluno = dict()
aluno['nome'] = input('Nome: ').title()
aluno['media'] = float(input('Média Do Aluno:'))
if(aluno['media'] >= 7):
    aluno['situacao'] = '\033[32mAprovado'
elif(aluno['media'] >= 5):
    aluno['situacao'] = '\033[33mRecuperação'
else:
    aluno['situacao'] = '\033[31mReprovado'
print('-='*40)
for k, v in aluno.items():
    print(f' - {k} É Igual A {v}')
    