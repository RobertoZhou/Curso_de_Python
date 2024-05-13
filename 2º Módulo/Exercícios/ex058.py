from time import sleep
from random import randint
contador = 1
numAleatorio = randint(1, 10)
print("{:=^40}".format("[ JOGO ADIVINHA ]"))
sleep(1)
print('Sou Seu Computador...')
sleep(1)
print('Acabei De Pensar Em Um Número Entre 0 e 10.')
sleep(1)
print('Será Que Você Consegui Adivinhar Qual Foi?')
sleep(0.5)
num = int(input("Qual É Seu Palpite? "))
while num != numAleatorio:
    if(num > numAleatorio):
        print('Menos... Tente Mais Uma Vez!')
        num = int(input('Qual Seu Palpite? '))
    elif(num < numAleatorio):
        print('Mais... Tente Mais Uma Vez!')
        num = int(input('Qual Seu Palpite? '))
    contador += 1
print('Número: {}'.format(numAleatorio))
print('Acertou Com {} Tentativas. Parabéns!'.format(contador))