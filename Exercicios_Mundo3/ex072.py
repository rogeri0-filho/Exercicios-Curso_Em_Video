from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10))

print('listagem dos números: ', end='')

for n in tupla:
    print(f'{n} ', end='')

print(f'\nMaior valor: {max(tupla)}')
print(f'Menor valor:  {min(tupla)}')
