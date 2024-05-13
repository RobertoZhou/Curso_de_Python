from time import sleep
c = ('\033[m',  #0 - Sem Cor
     '\033[0;37;40m', #1 - branco
     '\033[0;30;41m', #2 - Cor Vermelho
     '\033[0;30;42m', #3 - Cor Verde
     '\033[0;30;43m', #4 - Cor Amarelo
     '\033[0;30;44m', #5 - Cor Azul
     '\033[0;30;45m', #6 - Cor Roxo
     '\033[0;30;46m', #7 - Cor Azul-Claro
     '\033[0;30;47m' #8 - Cor Cinza
     )

def titulo(msg, cor=0):
    cont = len(msg) + 4
    print(c[cor], end='')
    print('~' * cont)
    print(f"{msg :^{cont}}")
    print('~' * cont)
    print(c[0], end='')
    sleep(1)

def ajuda(com):
    titulo(f'Acessando o manual de comando \'{com}\'', 5)
    print(c[1])
    help(com)
    sleep(2)

#Programa principal

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 3)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 2)