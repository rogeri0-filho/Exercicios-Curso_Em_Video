produtos = ('Borracha', 1.50, 'Lápis', 1.75, 'Caneta', 1.75,
             'Estojo', 25.50, 'Transferidor', 11.00, 'Compasso', 15.00,
             'Mochila', 130.66, 'Livro', 83.00)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')

print('-' * 40)
