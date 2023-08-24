print("="*6, "DESAFIO 022", "="*6)

nome = str(input("Digite seu Nome: ")).strip()
print("Maiúsculo: {}".format(nome.upper()))
print("Minúsculo: {}".format(nome.lower()))
print("Quantas Letras Tem o Nome: {}".format(len(nome.replace(" ", ""))))
quantidade = nome.split()
print("Quantas Letras Tem o Primeiro Nome: {}".format(len(quantidade[0])))