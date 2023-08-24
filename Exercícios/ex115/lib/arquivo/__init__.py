from ex115.lib.interface import cabeçalho
def arquivoExiste(nome):
    try:
        with open(nome, 'r') as arquivo:
            arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarArquivo(nome):
    try:
        with open(nome, 'wt+') as novo:
            novo.close()
    except:
        print('Houve Um Erro Na Criação Do Arquivo!')
    else:
        print(f'Arquivo {nome} Criado Com Sucesso!')

def lerArquivo(nome):
    try:
        ler = open(nome, 'r')
    except:
        print('ERRO Ao Ler O Arquivo!')
    else:
        cabeçalho('Pessoas Cadastradas')
        for linha in ler:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} Anos')
    finally:
        ler.close()

def cadastrar(arquivo, nome='<Desconhecido>', idade=0):
    try:
        a = open(arquivo, 'a')
    except:
        print('Houve Um ERRO Na Abertura Do Arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve Um ERRO Na Hora De Escrever Os Dados!')
        else:
            print(f'Novo Registro De {nome} Adicionado!')
            a.close()