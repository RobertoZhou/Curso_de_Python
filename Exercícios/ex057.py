sexo = str(input("Informe Seu Sexo [M/F]: ")).upper().strip()[0]
while sexo not in "MF":
    sexo = str(input("Dados Inválidos. Por Favor, Informe Seu Sexo [M/F]: ")).upper().strip()[0]
if(sexo == "M"):
    print("Sexo \033[31m{}\033[m Registrado Com Sucesso!!!".format("Masculino"))
else:
    print("Sexo {} Registrado Comm Sucesso!!!".format("Feminino"))