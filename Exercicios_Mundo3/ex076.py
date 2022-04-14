'''
lista = []

for c in range(0, 5):
    lista.append(int(input('Digite um valor para guarda-lo na lista: ')))

lista.sort()

print('-=' * 21)
print(f'O menor valor foi {lista[0]} na posição {lista.index(lista[0])}')
print(f'O maior valor foi {lista[-1]} na posição {lista.index(lista[-1])}')
'''

lista = []
maior = 0
menor = 0

for c in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print('-=' * 21)
print(f'Você digitou os valores {lista}!')
print('-=' * 21)

print(f'O maior falor foi {maior} nas posições ', end='')
for posicoes, v in enumerate(lista):
    if v == maior:
        print(f'{posicoes}...', end='')
print()

print(f'O menor valor foi {menor} nas posições ', end='')
for posicoes, v in enumerate(lista):
    if v == menor:
        print(f'{posicoes}...', end='')
print()
