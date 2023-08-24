print("="*6, "DESAFIO 015", "="*6)

dias = int(input("Quantos dias: "))
km = float(input("Quantos Km: "))
pago = (dias * 60) + (km * 0.15)
print("O total a Pagar é de R${:.2f}".format(pago))
