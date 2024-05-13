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