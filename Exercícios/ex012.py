print("="*6, "DESAFIO 012", "="*6)

produto = float(input("Digite o Preço de um Produto: R$"))
desconto = produto - (produto * 5 /100)
print("O Preço Do Produto com 5% de Desconto é de {:.2f}".format(desconto))