def alinhamento(frase):
    linha = len(frase) + 4
    print('~' * linha)
    print(f'{frase :^{linha}}')
    print('~' * linha)
alinhamento('Olá, Mundo')
alinhamento('Gustavo Guanabara')
alinhamento('Curso De Python No YouTube')
alinhamento('CeV')