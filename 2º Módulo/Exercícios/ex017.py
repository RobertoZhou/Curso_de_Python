print("="*6, "DESAFIO 017", "="*6)

from math import hypot
z = float(input("Digite o Comprimento do Cateto Oposoto: "))
x = float(input("Digite o Comprimento do Cateto Adjacente: "))
hip = hypot(x, z)
print("O Comprimento da Hipotenusa é {:.2f}".format(hip))
