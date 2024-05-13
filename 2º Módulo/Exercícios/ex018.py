print("="*6, "DESAFIO 018", "="*6)

from math import sin, cos, tan, radians
num = float(input("Digite um Número para ver seu Seno, Cosseno e Tangente: "))
print("Seno: {}".format(sin(radians(num))))
print("Cosseno: {}".format(cos(radians(num))))
print("Tangente: {}".format(tan(radians(num))))
