print("="*6, "\033[2;31mDESAFIO 043\033[m", "="*6)

from time import sleep

print("="*20)
print("\033[4;36mANALISADOR DE IMC\033[m")
print("="*20)

sleep(1)

peso = float(input("Digite Seu Peso: "))
altura = float(input("Digite Sua Altura: "))
imc = peso / (altura ** 2)

if(imc < 18.5):
    print("Abaixo de 18.5: Abaixo Do Peso!")
elif(imc >= 18.5) and (imc < 25):
    print("Entre 18.5 a 25: Peso Ideal!")
elif(25 <= imc < 30):
    print("25 até 30: Sobrepeso")
elif(30 <= imc < 40):
    print("30 até 40: Obsidade")
else:
    print("Acima de 40: Obsidade Mórbida")
