def leiaInt(msg):
    global continuar, n2
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            print('\nO úsuario Decidiu não informar o número!')
            continuar = False
            n2 = 0
            return 0
        except:
            print('\033[31mERRO : Por favor, digite um número inteiro valido.\033[m')
            continue
        else:
            continuar = True
            return num


def leiaFlaot(msg):
    global continuar, n2
    while True:
        try:
            num = float(input(msg))
        except KeyboardInterrupt:
            print('\nO úsuario Decidiu não informar o número!')
            continuar = False
            return 0
        except:
            print('\033[31mERRO : Por favor, digite um número real valido.\033[m')
        else:
            continuar = True
            return num


n1 = leiaInt('Digite Um Número Inteiro: ')
if continuar:
    n2 = leiaFlaot('Digite Um Número Real: ')

print(f'O valor inteiro digitado foi {n1} e o real foi {n2}.')