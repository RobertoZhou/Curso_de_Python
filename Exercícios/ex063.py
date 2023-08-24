print('-'*45)
print('Sequência de Fibonacci')
print('-'*45)
n = int(input('Quantos Termos Você Quer Mostrar? '))
cont = 1
antigo = 0
atual = 1
fibonacci = 0
while cont <= n:
    print('{}'.format(fibonacci), end = " → ")
    antigo = atual
    atual = fibonacci
    fibonacci = antigo + atual
    cont += 1
print('Fim')
