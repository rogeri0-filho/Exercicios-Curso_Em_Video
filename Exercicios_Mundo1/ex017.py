from random import choice

lista = list()
for c in range(0, 4):
    aluno = str(input(f'Digite o nome do {c+1}º aluno: '))
    lista.append(aluno[:])

print(f'O aluno escolhido foi: {choice(lista)}')
