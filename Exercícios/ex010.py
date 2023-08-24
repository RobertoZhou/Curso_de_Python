print("="*6, "DESAFIO 010", "="*6)

dinheiro = float(input("Digite Quanto Dinheiro tem na sua Carteira: R$"))
dolares= dinheiro / 3.27
print("Com R${:.2f}, Você Pode Comprar até ${:.2f}".format(dinheiro, dolares))