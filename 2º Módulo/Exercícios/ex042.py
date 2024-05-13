print("="*6, "\033[2;31mDESAFIO 042\033[m", "="*6)

r1 = float(input("Primeira Reta: "))
r2 = float(input("Segundo Reta: "))
r3 = float(input("Terceira Reta: "))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print("\033[2;31mOs Segmentos Acima Podem Formar Um Triângulo!")
    if(r1 == r2) and (r2 == r3):
        print("\033[2;32mEQUILÁTERO:  Todos os Lados São Iguais!!")
    elif(r1 == r2) or (r1 == r3) or (r2 == r3):
     print("\033[2;33mISÓSCELES: Os Dois Lados São Iguais, Um Diferente!!")
    else:
        print("\033[2;34mESCALENO: Todos Os Lados São Diferentes!!")
else:
    print("\033[2;35mOs Segmentos Acima Não Podem Formar um Triangulo!")