def leiaInt(num):
    while True:
        valor = input(num).strip()
        if valor.isnumeric():
            valor = int(valor)
            break
        else:
            print('\033[31mERRO! Digite Um Número Inteiro Valido.\033[m')
    return valor


#Programa principal0
n = leiaInt('Digite um número:')
print(f'Você Acabou De Digitar O Número {n}.')
    