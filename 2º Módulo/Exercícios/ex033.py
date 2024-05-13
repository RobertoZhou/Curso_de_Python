print("="*6, "DESAFIO 033", "="*6)

a = int(input("Primeiro Número: "))
b = int(input("Segundo Número: "))
c = int(input("Terceiro Número: "))

#Verificando o Maior Número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

#Verificando Menor Número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print("MAIOR: {}".format(maior))
print("Menor: {}".format(menor))
