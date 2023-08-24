def leiaDinheiro(msg):
    while True:
        p = input(msg).strip()
        if(p[::].isnumeric()):
            return float(p)
            break
        else:
            print(f'\033[31mERRO \"{p}\" é um preço INVÁLIDO!\033[m')