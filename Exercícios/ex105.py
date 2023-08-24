def notas(* valor, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param valor: Uma ou mais notas dos alunos (aceita varias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situações da turma.
    '''

    registro = dict()
    numeros = list()

    for i in valor:
        numeros.append(i)
    if numeros[-1] == True or numeros[-1] == False:
        numeros.pop()
    registro['total'] = len(numeros)
    registro['maior'] = max(numeros)
    registro['menor'] = min(numeros)
    registro['média'] = sum(numeros) / len(numeros)
    if sit == True or valor[-1]== True:
        if(registro['média'] >= 7):
            registro['situação'] = 'BOA'
        elif(registro['média'] < 7 is registro['média'] >= 6):
            registro['situação'] = 'RAZOÁVEL'
        else:
            registro['situação'] = 'RUIM'
    return registro

# Programa Principal
resp = notas(3.5, 2, 6.5, 2, 7, 4, False)
print(resp)
