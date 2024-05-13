print('\033[34m-' * 40)
print('{:^40}'.format('LOJA CURSO EM VIDEO'))
print('-' * 40, '\033[m')
total = produto_1k = precoBarato = 0
produtoBarato = ''
while True:
    produto = str(input('Nome Do Produto: ')).strip().title()
    while True:
        preco = input('Preço: R$')
        verifNum = preco.isdigit()
        if(verifNum == True):
            preco = float(preco)
            break
    total += preco
    if(preco > 1000):
        produto_1k += 1
    if(precoBarato == 0) or (preco < precoBarato):
        precoBarato = preco
        produtoBarato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("Quer Continuar? [S/N] ")).strip().upper()[0]
    if(continuar == 'N'):
        break
print('{:=^40}'.format(' FIM DO PROGRAMA '))
print(f'O Total Da Compra Foi R${total}')
print(f'Temos {produto_1k} Produtos Custando Mais de R$1000.00')
print('O Produto Mais Barato Foi {} Que Custa R${:.2f}'.format(produtoBarato, precoBarato))
