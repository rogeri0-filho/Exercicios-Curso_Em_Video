from random import shuffle

lista = list()
for c in range(0, 4):
    aluno = str(input(f'Digite o nome do {c+1}º aluno: '))
    lista.append(aluno[:])

shuffle(lista)
print(f'A ordem de chamda é: {lista}')
