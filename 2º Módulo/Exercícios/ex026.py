print("="*6, "DESAFIO 026", "="*6)

palavra = str(input("Digite Uma Frase: ")).upper().strip()
print("A Palavra Possui: {} a Letra A".format(palavra.count("A")))
print("A Letra A Aparece primeiro na Posição: {}".format(palavra.find("A")+1))
print("A Letra A Aparece no Final na Posição: {}".format(palavra.rfind("A")+1))
