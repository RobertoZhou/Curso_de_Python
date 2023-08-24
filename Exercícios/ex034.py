print("="*6, "DESAFIO 034", "="*6)

salario = float(input("Digite O Valor de um Salário: R$"))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print("Com o Aumento de 10%, O Salário passa a ser de R${:.2f}".format(aumento))
else:
    aumento = salario + (salario * 15 / 100)
    print("Com o Aumento de 15%, O Salário passa a ser de R${:.2f}".format(aumento))