nome = ""
maiorIdadeM = 0
idadeSexoF = 0
somaDasIdade = 0
for p in range(1, 5):
    print("{0} {1}ª PESSOA {0}".format("-"*5, p))
    nomeP = str(input("Nome: ")).title().strip()
    idadeP = int(input("Idade: "))
    sexoP = str(input("Sexo [M/F] : ")).upper().strip()
    somaDasIdade += idadeP
    if(idadeP > maiorIdadeM and sexoP == "M"):
        nome = nomeP
        maiorIdadeM = idadeP
    if(sexoP == "F" and idadeP <= 20):
        idadeSexoF += 1
print("A Média De Idade Do Grupo É De {:.2f} Anos".format(somaDasIdade / 4))
print("O Homem Mais Velho tem {} Anos E  Se Chama {}".format(maiorIdadeM, nome))
print("Ao Todo São {} Mulheres Com Menos De 20 Anos".format(idadeSexoF))