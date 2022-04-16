'''
from time import sleep

lista1 = list()
lista2 = list()

for contador in range(0, 7):
    valores = int(input('Digite um valor: '))

    if valores % 2 == 0:
        lista1.append(valores)
    elif valores % 2 == 1:
        lista2.append(valores)

lista1.sort()#sorteia a lista 1
lista2.sort()#sorteia a lista 2

print('--' * 30)
print('ORDENANDO SUA LISTA...')
print('--' * 30)
sleep(2)
print(f'Lista de valores pares: {lista1}!')
print(f'Lista de valores impares: {lista2}!')
print('--' * 30)
'''

from time import sleep

lista = [[], []]
valores = 0

for cont in range(1, 8):
    valores = int(input(f'Digite o {cont}º valor: '))

    if valores % 2 == 0:
        lista[0].append(valores)
    elif valores % 2 == 1:
        lista[1].append(valores)

lista[0].sort()
lista[1].sort()

print('--' * 30)
print('ORDENANDO SUA LISTA...')
print('--' * 30)
sleep(2)
print(f'Lista de valores pares: {lista[0]}!')
print(f'Lista de valores impares: {lista[1]}!')
print('--' * 30)
