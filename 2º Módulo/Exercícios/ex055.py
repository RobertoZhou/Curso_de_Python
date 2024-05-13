menorPeso = 0
maiorPeso = 0
for pessoa in range(1, 6):
    peso = float(input("Peso da {}ª Pessoa: ".format(pessoa)))
    if(pessoa == 1):
        menorPeso = peso
        maiorPeso = peso
    if(peso > maiorPeso):
            maiorPeso = peso
    if(peso < menorPeso):
            menorPeso = peso
print("Maior Peso: {}".format(maiorPeso))
print("Menor Peso: {}".format(menorPeso))