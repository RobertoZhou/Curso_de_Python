print("="*6, "\033[4;31;31mDESAFIO 038\033[m", "="*6)

n1 = int(input("Digite Um Número: "))
n2 = int(input("Digite Outro Número: "))
if n1 > n2:
    print("\033[1;33mOPrimeiro Valor: {}, é Maior!".format(n1))
    print("\033[1;33mOSegundo Valor: {}, é Menor!".format(n2))
elif n2 > n1:
    print("\033[1;35mPrimeiro Valor: {}, é Menor!".format(n1))
    print("\033[1;35mO Segundo Valor: {}, é Maior1".format(n2))
else:
    print("\033[1;36mOs Dois Valores São Iguais!")