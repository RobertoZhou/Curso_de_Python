print("="*6, "\033[2;31mDESAFIO 044\033[m", "="*6)

from time import sleep
print("{:=^40}".format(" LOJA "))
sleep(1)
preco = float(input("Preço Das Comprars: R$ "))
pagamento = int(input("""FORMAS DE PAGAMENTO
[ 1 ] À Vista Dinherio/Cheque
[ 2 ] À Vista Cartão
[ 3 ] 2x No Cartão
[ 4 ] 3x Ou Mais No Cartão
Qual É A Opção? """))

sleep(1.5)
if(pagamento == 1) or (pagamento == 2) or (pagamento == 3) or (pagamento == 4):
    if(preco == 1):
        total = preco - (preco * 10 / 100)
    elif(preco == 2):
        total = preco - (preco * 5 / 100)
    elif(preco == 3):
        total = preco
        parcela = total / 2
        print("Sua Compra Será Parcelada em 2x de {:.2f}".format(parcela))
    elif(preco == 4):
        total = preco (preco * 20 / 100)
        totalParcela = int(input("Quantas Parcelas? "))
        parcela = total / totalParcela
        print("Sua Compra Será Parcelada em {}x de R${:.2f} COM JUROS.".format(totalParcela, parcela))
    print("Sua Compra de R${:.2f}, Vai Custar R${:.2f} No Final.".format(preco, total))
else:
    print("OPÇÃO INVALIDA!!!")