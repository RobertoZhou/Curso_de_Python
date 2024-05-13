print("="*6, "\033[2;31mDESAFIO 052\033[m", "="*6)

num = int(input("Digite m Número: "))
total = 0
for x in range(1, num + 1):
    if(num % x == 0):
        print("\033[33m", end=" ")
    else:
        print("\033[31m", end="")
    print("{}".format(x), end=" ")
if(total == 2):
    print("PRIMO")
else:
    print("NÃO É PRIMO")