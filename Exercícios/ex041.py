print("="*6, "\033[2;31mDESAFIO 041\033[m", "="*6)

from datetime import date
ano = int(input("Digite em Que Ano Nasceu: "))

anoAtual = date.today().year

idade = anoAtual - ano

print("Idade: {}".format(idade))
if idade <= 9:
    print("\033[2;31mMirim!!!")
elif idade <= 14:
    print("\033[2;32mInfantil!!!")
elif idade <= 19:
    print("\033[2;33mJunior!!!")
elif idade <= 25:
    print("\033[2;34mSenior!!!")
else:
    print("\033[2;35mMaster!!!")