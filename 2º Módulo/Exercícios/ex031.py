print("="*6, "DESAFIO 031", "="*6)

km = float(input("Digite Quantos Km: "))
if km <= 200:
    menor = km * 0.50
    print("O Valor da Viagem, é de R${:.2f}".format(menor))
else:
    maior = km * 0.45
    print("O Valor da Viagem, é de R${:.2f}".format(maior))