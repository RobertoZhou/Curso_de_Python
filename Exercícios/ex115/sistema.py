from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arquivo = 'infomação.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resp = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair Do Sistema'])
    if(resp == 1):
        #Opção listar o conteúdo de um arquivo.
        lerArquivo(arquivo)
    elif(resp == 2):
        #Opção de cadastrar uma nova pessoa.
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif(resp == 3):
        cabeçalho('Saindo Do Sistema .... Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite Uma oOpção Válida.\033[m')
    sleep(0.5)