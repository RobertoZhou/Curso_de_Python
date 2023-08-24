print("="*6, "\033[2;31mDESAFIO 048\033[m", "="*6)

soma = 0
contador = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        soma = soma + x
        contador = contador + 1
print("A Soma de Todos os {} Valores, é {}".format(contador, soma))
