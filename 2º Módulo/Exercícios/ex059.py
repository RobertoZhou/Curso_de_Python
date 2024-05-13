from time import sleep
opcao = 0
valor1 = int(input("Primeiro Valor: "))
valor2 = int(input("Segundo Valor: "))
sleep(1)
while opcao != 5:
    print("{}".format("-=" * 15))
    sleep(0.5)
    print("""
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair Do Programa""")
    sleep(0.5)
    opcao = int(input(">>>>> Qual É A Sua Opção? "))
    sleep(0.5)
    if(opcao == 1):
        print("A Soma Entre {} + {} É {}".format(valor1, valor2, valor1 + valor2))
    elif(opcao == 2):
        print("O Resultado De {} X {} É {}".format(valor1, valor2, valor1 * valor2))
    elif(opcao == 3):
        if(valor1 > valor2):
            print("Entre {0} É {1} O Maior Valor É {0}".format(valor1, valor2))
        elif(valor2 > valor1):
            print("Entre {0} É {1} O Maior Valor É {1}".format(valor1, valor2))
    elif(opcao == 4):
        print("Informe Os Números Novamente:")
        valor1 = int(input("Primeiro Valor: "))
        valor2 = int(input("Segundo Valor: "))
    elif(opcao != 5):
        print("Opção Invalida. Tente Novamente!")
        sleep(0.5)
print("Finalizando...")
sleep(1)
print("FIM DO PROGRAMA")