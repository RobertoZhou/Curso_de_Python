print("="*6, "DESAFIO 027", "="*6)

n = str(input("Digite Um Nome: ")).strip()
nome = n.split()
print("Primeiro Nome: {}".format(nome[0]))
print("Ultimo Nome: {}".format(nome[len(nome)-1]))