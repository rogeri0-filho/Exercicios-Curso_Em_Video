ficha = list()

while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media]) #nome[0], notas[1], media[2]

    resposta = str(input('Deseja continuar? [S/N]')).upper()
    if resposta == 'N':
        break

print('-=' * 30)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('--' * 30)

for indice, aluno in enumerate(ficha):
    print(f'{indice+1:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('--' * 30)
    opçao = int(input('Qual aluno você deseja mostrar as notas? (999break):'))

    if opçao == 999:
        print('FINALIZANDO...')
        break
    if opçao <= len(ficha) - 1:
        print(f'Notas de {ficha[opçao][0]} são {ficha[opçao][1]}')
print('VOLTE SEMPRE!')



