from random import randint
from time import sleep

pc = randint(0, 5)

print('-=-' * 20)
print('Vou sortear um número entre 0 e 5, tente advinhar qual será!!')
print('-=-' * 20)
print('LOADING...')

sleep(3)

player = int(input('Em que número eu pensei? '))

if player == pc:
    print('Parabéns! Você advinhou o número sorteado.')

else:
    print('Você não advinhou o número sorteado, tente novamente.')
    print(f'Eu pensei no número {pc} e não no {player}.')