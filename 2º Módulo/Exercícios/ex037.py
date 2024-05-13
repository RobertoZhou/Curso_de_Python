print("="*6, "\033[4;31;31mDESAFIO 037\033[m", "="*6)
from time import sleep
num = int(input("Degite um Número Inteiro: "))
print("\033[2;33mGostaria De Converte o Número? (s/n)")
verificacao = str(input("R: ")).upper()

if verificacao == "S":
    print("[ 1 ] BINÁRIO")
    print("[ 2 ] OCTAL")
    print("[ 3 ] HEXADECIMAL")
    escolha = int(input("Sua Opção: "))
    sleep(0.5)
    print("\033[2;31mLoading...\033[m")
    sleep(1)
    if(escolha == 1):
        print("BINÁRIO:", bin(num) [2:])
    elif(escolha == 2):
        print("OCTAL:", oct(num)[2:])
    elif(escolha == 3):
        print("HEXADECIMAL:", hex(num)[2:])
    else:
        print("\033[2;35mOpção Inválido . Tente Novamente")
print("\033[3;32;32mPrograma Finalizado!!!")