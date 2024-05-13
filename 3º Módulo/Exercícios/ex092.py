from datetime import datetime
ano = datetime.now().year
registro = {'nome':str(input('Nome: ').title()), 'idade':(ano - int(input('Ano De Nascimento:'))),
            'ctps':int(input('Carteira De Trabalho (0 Não Tem): '))}
if(registro['ctps'] != 0):
    registro['contratação'] = int(input('Ano De Contratação: '))
    registro['salario'] = float(input('Salário: R$'))
    registro['aposentadoria'] = registro['idade'] + ((registro['contratação'] + 35) - ano)
print('='* 40)
print(registro)
for k, v in registro.items():
    print(f'    - {k.title()} Tem O Valor De {v}')
