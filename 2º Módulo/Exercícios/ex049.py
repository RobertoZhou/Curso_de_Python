print("="*6, "\033[2;31mDESAFIO 049\033[m", "="*6)

tabuada = int(input("Digite Um Número Para Ver Sua Tabuada: "))
contador = 0
for c in range(0, tabuada * 10 + 1, tabuada):
    print("{} x {} = {}".format(tabuada, contador, c))
    contador = contador + 1