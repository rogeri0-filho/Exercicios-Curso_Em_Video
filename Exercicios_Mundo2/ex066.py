from random import randint

cont = 0

while True:
    print('-' * 50)
    player = int(input('Escolha um número: '))
    pc = randint(0, 10)
    soma = pc + player
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print('-' * 50)
    if tipo == 'P':
        if soma % 2 == 0:
            cont += 1
            print(f'Você jogou {player} e escolheu Par, e o computador jogou {pc}. Total {soma} por tanto, é Par!')
            print('-' * 50)
            print('Você Ganhou!')
        else:
            print(f'Você jogou {player} e escolheu Par, e o computador jogou {pc}. Total {soma} por tanto, é Ímpar')
            print('-' * 50)
            print('Você perdeu.')
            print('=-=' * 27)
            print(f'FIM DE JOGO. Você conquistou um total de {cont} vitórias')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            cont += 1
            print(f'Você jogou {player} e escolheu Ímpar, e o computador jogou {pc}. Total {soma} por tanto, é Ímpar!')
            print('-' * 50)
            print('Você Ganhou!')
        else:
            print(f'Você jogou {player} e escolheu Ímpar, e o computador jogou {pc}. Total {soma} por tanto, é Par!')
            print('-' * 50)
            print('Você perdeu.')
            print('=-=' * 27)
            print(f'FIM DE JOGO. Você conquistou um total de {cont} vitórias')
            break

print('=-=' * 27)
