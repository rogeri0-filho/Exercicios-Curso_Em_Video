lista = list()

while True:
    valores = int(input('Digite um valor para armazena-lo na lista: '))
    if valores not in lista:
        lista.append(valores)
        print('Valor adicionado com sucesso...')

    else:
        print('Valores duplicados não são aceitos!')
    resposta = str(input('Deseja continuar [S/N]?: ')).upper()

    if resposta == 'N':
        break

lista.sort()

print('-=' * 40)
print(f'Os elementos da sua lista são: {lista}!')
print('-=' * 40)
