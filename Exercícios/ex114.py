import requests

def verificar_internet():
    url = 'http://pudim.com.br/'
    try:
        requests.get(url)
    except:
        print('Não Foi Possivel Acessar O Site Pudim.')
    else:
        print('O Site Pudim Foi Acessado Com Sucesso.')
verificar_internet()