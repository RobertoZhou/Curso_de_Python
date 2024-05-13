valores = []
print('=-' * 40)
while True:
    valor = int(input("Digite Um Valor: "))
    if(valor not in valores):
        valores.append(valor)
        print('\033[30:42mValor Adicionado Com Sucesso...\033[m')
    else:
        print('\033[30:41mValor Duplicado! Não Vou Adicionar... \033[m')
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input("Quer Continuar? [\033[32mS\033[m/\033[31mN\033[m] "))
    if(resp in 'Nn'):
        break
print('=-' * 40)
valores.sort()
print(f'Você Digitou Os Valores: {valores}')