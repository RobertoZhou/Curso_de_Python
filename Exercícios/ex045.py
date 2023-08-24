print("="*6, "\033[2;31mDESAFIO 045\033[m", "="*6)

from time import sleep
from random import randint
opcoes = ("PEDRA", "PAPEL", "TESOURA")
bot = randint(0, 2)
jogador = int(input("""Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Sua Opção: """))
sleep(1)
print("=-=-" * 20)
print("JOGADOR = {}".format(opcoes[jogador]))
print("BOT = {}".format(opcoes[bot]))
print("=-=-" * 20)
sleep(1)
if jogador == 0:
    if bot == 0:
        print("EMPATE!!!")
    elif bot == 1:
        print("VOCÊ PERDEU!!!")
    elif bot == 2:
        print("VOCÊ VENCEU!!!")

elif jogador == 1:
    if bot == 0:
        print("VOCÊ VENCEU!!!")
    elif bot == 1:
        print("EMPATE!!!")
    elif bot == 2:
        print("VOCÊ PERDEU!!!")

elif jogador == 2:
    if bot == 0:
        print("VOCÊ PERDEU!!!")
    elif bot == 1:
        print("VOCÊ VENCEU!!!")
    elif bot == 2:
        print("EMPATE")
