from random import randint
from time import sleep

jogos = list() #lista que vai receber todas as listas sorteadas
lista = list() #lista que vai armazenar os numeros sorteados
totaljg = 1    #total de jogos que vão ser sorteados

print('--' * 18)
print('       SORTERIO DA MEGA SENA')
print('--' * 18)

jogadas = int(input('Quantos jogos você deseja sortear?'))

while totaljg <= jogadas:
    contador = 0  # variavel que vai verificar a quantidade de jogos que deve ser feito
    while True:
        numsort = randint(1, 60) #variavel que vai sortear os números

        if numsort not in lista: #verifica se o numero sorteado está na lista para evitar repetições
            lista.append(numsort) #caso não estaja, ele é adicionado
            contador += 1

        if contador >= 6:
            break #Quebra o loop infinito

    lista.sort() #Poe os valores da lista em ordem crescente
    jogos.append(lista[:]) #Cria uma copia da lista em jogos
    lista.clear() #Apaga a lista
    totaljg += 1 #Para o loop infinito

print('==' * 3, f'SORTEANDO {jogadas} JOGOS', '==' * 3)

for indice, lis in enumerate(jogos):
    print(f'Jogo {indice + 1}: {lis}')
    sleep(1)

print('==' * 5, '<BOA SORTE>', '==' * 5)
