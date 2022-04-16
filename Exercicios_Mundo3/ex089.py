from random import randint
from time import sleep
from operator import itemgetter

jogos = {'Jogador 1' : randint(1, 6),
         'Jogador 2' : randint(1, 6),
         'Jogador 3' : randint(1, 6),
         'Jogador 4' : randint(1, 6)}

ranking = list()

print('======JOGOS SORTEADOS=======')

for k, v in jogos.items():
    sleep(1)
    print(f'O {k} tirou: {v} no dado.')

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print('====RANKING DOS JOGADORES====')

for i, v in enumerate(ranking):
    print(f'   {i+1}º Lugar: {v[0]} com {v[1]}')
print('--' * 14)
