tabela = ('Palmeiras', 'Corinthians', 'Athletico-PR', 'Internacional', 'Atlético-MG', 'Santos',
           'Flamengo', 'Fluminense', 'Botafogo', 'São Paulo', 'Bragantino', 'Avaí', 'Atlético-GO',
           'Ceará' ,'Coritiba' ,'América-MG', 'Goiás', 'Cuiabá', 'Fortaleza', 'Juventude')
print('=-' * 40)
print(f'Lista do Time do Brasileirão: {tabela}')
print('=-' * 40)
print(f'Os 5 Primeiros São: {tabela[:5]}')
print('=-' * 40)
print(f'Os Quatros Ultimos são: {tabela[-4:]}')
print('=-' * 40)
print(f'Times Em Ordem Alfabética: {sorted(tabela)}')
print('=-' * 40)
print('O Chapecoense Está na {}ª Posição'.format(tabela.index('Bragantino')))
