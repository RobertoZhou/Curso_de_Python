print("="*6, "DESAFIO 036", "="*6)

casa = float(input("Digite o Valor da Casa: R$"))
salario = float(input("Digite o Salário do Comprador: R$"))
anos = int(input("Digite Quantos Anos Irá Pagar: "))
minimo = salario * 30 / 100

prestacao = casa / (anos * 12)
if prestacao <= minimo:
    print("\033[2;34mEmprestimo pode ser CONCEDIDO.")
else:
    print("\033[2;31mEmprestimo NEGADO.")
