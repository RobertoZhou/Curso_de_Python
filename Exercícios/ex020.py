print("="*6, "DESAFIO 020", "="*6)

from random import shuffle
aluno1 = input("1°Aluno: ")
aluno2 = input("2°Aluno: ")
aluno3 = input("3°Aluno: ")
aluno4 = input("4°Aluno: ")
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print(lista)
