from random import randint

lista = list()

def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(0, 10))
    print(f'Os números sorteados foram {lista}')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somandos os valores pares, temos: {soma}')



#PROGRAMA PRINCIPAL
sorteia(lista)
somapar(lista)

