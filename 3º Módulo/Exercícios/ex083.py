expr = str(input('Digite A Expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if(len(pilha) > 0):
            pilha.pop()
        else:
            pilha.append(')')
if(len(pilha) == 0):
    print('Sua Expressão É Valida!')
else:
    print('Sua Expressão Está Errada!')