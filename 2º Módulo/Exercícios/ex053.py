"""
frase = str(input("Digite Uma Frase: ")).upper().replace(" ", "")
print("Frase Invertida: {}".format(frase[::-1]))
if(frase == frase[::-1]):
    print("A Frase Digitada É Um \033[34mPALÍNDROMO!")
else:
    print("A Frase Digitada Não É Um \033[31mPALÍNDROMO!")
"""
frase = str(input("Digite Uma Frase: ")).replace(" ", "").upper()
inverso = ""
for letras in range(len(frase) -1, -1, -1):
    inverso += frase[letras]
print("Frase Invertida: {}".format(inverso))
if(inverso == frase):
    print("\033[34mEstá Frase É Um PALÍNDROMO!")
else:
    print("\033[31mEstá Frase Não É Um PALÍNDROMO!")