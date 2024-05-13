def leiaDinheiro(msg):
    while True:
        p = input(msg).strip().replace(',', '.').strip()
        if p.isalpha() or p == '':
            print(f'\033[31mERRO \"{p}\" é um preço INVÁLIDO!\033[m')
        else:
            return float(p)