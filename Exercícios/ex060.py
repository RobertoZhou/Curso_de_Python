from time import sleep
n1 = int(input("""Digite Um Número.
Calcular Seu Fatorial: """))
fatorial = n1
resultado = n1
sleep(0.5)
print("Calculando {}! = ".format(fatorial), end = "")
while(n1 != 1):
    print(n1, end = " x ")
    n1 -= 1
    resultado *= n1
print("1 = {}".format(resultado))
