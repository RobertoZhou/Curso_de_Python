def resumo(p, aumento = 0, reducao = 0):
    print(f'-' * 30)
    print(f"{'RESUMO DO VALOR' :^30}")
    print(f'-' * 30)
    print(f'Preço Analisado: \t{moeda(p):>}')
    print(f'Dobro Do Preço: \t{dobro(p, True):>}')
    print(f'Metade Do Preço: \t{metade(p, True):>}')
    print(f'{aumento}% De Aumento: \t{aumentar(p, aumento, True):>}')
    print(f'{reducao}% De Redução: \t{diminuir(p, reducao, True):>}')
    print('-' * 30)

def moeda(preco, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def metade(p, prefixo = False):
    calc = p / 2
    if(prefixo == True):
        return moeda(calc)
    return calc

def dobro(p, prefixo = False):
    calc = p * 2
    if (prefixo == True):
        return moeda(calc)
    return calc

def aumentar(p, valor, prefixo = False):
    calc = p + (p/100 * valor)
    if (prefixo == True):
        return moeda(calc)
    return calc

def diminuir(p, valor, prefixo = False):
    calc = p - (p/100 * valor)
    if (prefixo == True):
        return moeda(calc)
    return calc