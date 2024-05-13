print("="*6, "\033[2;31mDESAFIO 039\033[m", "="*6)

from datetime import date
genero = int(input("""Qual Seu Gênero:\n[ 1 ] HOMEM\n[ 2 ] MULHER\nOpção: """))
if(genero == 1):
    ano = int(input("Digite Em Ano Você Nasceu: "))
    idade = date.today().year - ano
    anosRestantes = 18 - idade
    anoDeAlistamento = ano + anosRestantes
    print("Quem Nasceu No Ano: {}, É Tem {} Anos.".format(ano, idade))
    if(idade == 18):
        print("Você Tem Que Se Alistar IMENDIATAMENTE")
    elif(idade < 18):
        print("Ainda Faltam {} Anos, Para O Seu Alistamento.".format(anosRestantes))
        print("Seu Alistamento Será No Ano: {} .".format(anoDeAlistamento))
    elif(idade > 18):
        print("Você Já Deveria Ter Se Alistado Há {} Anos.".format(idade - 18))
        print("Seu Alistamento Foi No Ano: {}.".format(date.today().year + anosRestantes))
else:
    print("Você Não Precisa Se Alistar.")