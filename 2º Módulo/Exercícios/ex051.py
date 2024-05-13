print("="*6, "\033[2;31mDESAFIO 051\033[m", "="*6)

termo = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
decimo = termo + (10 - 1) * razao
for x in range(termo, decimo + razao, razao):
    print("{}".format(x), end = " → ")
print("ACABOU")