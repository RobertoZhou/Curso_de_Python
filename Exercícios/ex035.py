print("="*6, "DESAFIO 035", "="*6)

print("-=-"*20)
print("Analisador de Triângulos")
print("-=-"*20)

r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro Segmento: "))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print("Os Segmentos Acima Podem Formar Um Triângulo")
else:
    print("Os Segmentos Acima Não Podem Formar Um Triângulo")