lista = list()

while True:
    entrada = lista.append(int(input('Digite um valor par guarda-lo em uma lista: ')))
    resposta = str(input('Deseja continuar [S/N]? ')).upper()
    if resposta == 'N':
        break

lista.sort(reverse=True)

print('--' * 30)
print(f'Você armazenou {len(lista)} elementos na lista!')
print(f'Esta é sua lista em ordem decrescente: {lista}! ')

if 5 in lista:
    print('O número 5 faz parte da sua lista!')
else:
    print('O número 5 não foi encontrado na sua lista!')
