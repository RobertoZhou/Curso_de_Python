print("="*6, "DESAFIO 032", "="*6)

from time import sleep
from datetime import date
ano = int(input(" (Para Analizar o Ano Atual digite 0)\nDigite o Ano que Gostaria de Analizar: "))

print("PROCESSANDO...")
sleep(2)
if ano == 0:
    ano = date.today().year

if((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0):
    print("O Ano {}, é BISSEXTO!!!".format(ano))

else:
    print("O Ano {}, NÃO é BISSEXTO!!!".format(ano))
