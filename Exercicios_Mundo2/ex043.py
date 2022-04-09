print('*+*' * 11)
print('{:^32}'.format('JO-KEN-PÔ'))
print('*+*' * 11)

from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')

print('Suas Opções:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA')
player = int(input('Qual sua jogada?'))
pc = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(0.5)

print('=-' * 20)
print('O Computador jogou {}!\nO Jogador jogou {}'.format(itens[pc], itens[player]))
print('=-' * 20)

if pc == 0:                                      #Computador escolhe PEDRA
    if player == 0:                              #Jogador escolhe PEDRA
        print('EMPATE! Os dois jogaram a mesma coisa.')
    elif player == 1:                            #Jogador escolhe PAPEL
        print('Vitória do JOGADOR!')
    elif player == 2:                            #Jogador escolhe TESOURA
        print('Vitória do COMPUTADOR!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 1:                                    #Computador escolhe PAPEL
    if player == 0:                              #Jogador escolhe PEDRA
        print('Vitória do COMPUTADOR!')
    elif player == 1:                            #Jogador escolhe PAPEL
        print('EMPATE! Os dois jogaram a mesma coisa.')
    elif player == 2:                            #Jogador escolhe TESOURA
        print('Vitória do JOGADOR!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 2:                                    #Computador escolhe TESOURA
    if player == 0:                              #Jogador escolhe PEDRA
        print('Vitória do JOGADOR!')
    elif player == 1:                            #Jogador escolhe PAPEL
        print('Vitória do COMPUTADOR!')
    elif player == 2:                            #Jogador escolhe TESOURA
        print('EMPATE! Os dois jogaram a mesma coisa.')
    else:
        print('JOGADA INVÁLIDA!')
