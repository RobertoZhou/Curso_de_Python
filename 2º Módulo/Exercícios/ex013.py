print("="*6, "DESAFIO 013", "="*6)

salario = float(input("Digite o Salário do Funcionário: R$"))
aumento = (salario + ((salario * 15)/100))
print("Com o Aumento de 15%, o Salário Passa a ser de R${:.2f}".format(aumento))