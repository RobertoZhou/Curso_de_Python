print("="*6, "\033[2;31mDESAFIO 050\033[m", "="*6)

soma = 0
for c in range(0, 6):
    n = int(input("Digite Um Número: "))
    if(n % 2 == 0):
        soma = soma + n
print("A Soma Dos Número PARES são: {}".format(soma))