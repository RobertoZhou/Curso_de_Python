print("="*6, "\033[2;31mDESAFIO 040\033[m", "="*6)

nota1 = float(input("\033[2;35mDigite A Primeira Nota: "))
nota2 = float(input("Digite A Segundo Nota:\033[2;35m "))

media = (nota1 + nota2) / 2

print("\033[2;35mMedia das Notas: {:.1f}".format(media))

if media >= 7:
    print("\033[2;32mAPROVADO!!!")
elif media >= 5 and media < 7:
    print("\033[2;34mRECUPERAÇÃO!!!")
else:
    print("\033[2;31mREPROVADO!!!")
