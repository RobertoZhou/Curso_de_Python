print("="*6, "DESAFIO 024", "="*6)

palavra = str(input("Digite o Nome de Uma Cidade: ")).strip().upper()
verificador = palavra.split()
print("Começa Com A Palavra Santo?: ".format(verificador[0] == "SANTO"))
