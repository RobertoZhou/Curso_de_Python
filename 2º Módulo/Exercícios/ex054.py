from datetime import date
anoAtual = date.today().year
maioresDeIdades = 0
menoresDeIdades = 0
for pessoa in range(1, 8):
    ano = int(input("Em Que Ano A {}ª Pessoa Nasceu? ".format(pessoa)))
    idade = anoAtual - ano
    if(idade >= 18):
        maioresDeIdades += 1
    elif(idade < 18):
        menoresDeIdades += 1
print("\033[35mAo Todo Tivemos {} Pessoas Maiores De Idades!".format(maioresDeIdades))
print("\033[36mE Também Tivemos {} Pessoas Menores De Idades!".format(menoresDeIdades))