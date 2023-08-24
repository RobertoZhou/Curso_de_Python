print("="*6, "DESAFIO 029", "="*6)

km = float(input("Digite a Velocidade do Veiculo: "))
if km > 80:
    multa = (km - 80) * 7
    print("MULTADO! Você Excedeu o Limite Permitido que é de 80Km/h.\nVocê Deve Pagar uma Multa de R${:.2f}".format(multa))
print("Tenha um Bom Dia, Dirija em Segurança!")
