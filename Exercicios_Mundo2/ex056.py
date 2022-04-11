from random import randint
from time import sleep

pc = randint(0, 10)
contador = 0

print('-=-' * 20)
print('Vou sortear um número entre 0 e 10, tente adivinhar qual será!!')
print('-=-' * 20)
print('LOADING...')

sleep(3)

player = int(input('Em que número eu pensei? '))

if player == pc:
    print('Parabéns! Você adivinhou o número sorteado.')

while player != pc:
    contador += 1
    print('Você errou, tente novamente!')
    player = int(input('Em que número eu pensei? '))

print(f'Você tentou {contador} vezes até acertar!')
