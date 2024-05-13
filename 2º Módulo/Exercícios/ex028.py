print("="*6, "DESAFIO 028", "="*6)

from random import randint
from time import sleep
num = randint(0, 5)
print("-=-"*15)
print("Adivinhe o Número Pensado entre 0 e 5!")
print("-=-"*15)
n = int(input("Qual foi o Número Pensado: "))
print("PROCESSANDO...")
sleep(2)
if n == num:
    print("VOCÊ ACERTOU!!!")
else:
    print("VOCE ERROU, O NÚMERO PENSADOR FOI {}!!!".format(num))