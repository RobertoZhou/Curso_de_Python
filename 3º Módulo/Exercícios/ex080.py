valores = []
for v in range(0, 5):
    valor = int(input("Digite Um Valor: "))
    if(v == 0) or (valor > max(valores)):
        valores.append(valor)
        print('Adicionado Ao Final Da Lista...')
    else:
        pos = 0
        while pos < len(valores):
            if(valor <= valores[pos]):
                valores.insert(pos, valor)
                print(f'Adicionado Na Posição {pos} Da Lista...')
                break
            pos += 1
print('=-' * 30)
print(f'Os Valores Digitados Em Ordem Foram: {valores}')