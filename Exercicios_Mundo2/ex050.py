n = int(input('Digite um número: '))
tot = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1

    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')

if tot == 2:
    print(f'\n\033[mO número {n} É um número PRIMO pois só foi dividido {tot} vezes!')
else:
    print(f'\n\033[mO número {n} NÃO é um número PRIMO pois foi dividido {tot} vezes!')
