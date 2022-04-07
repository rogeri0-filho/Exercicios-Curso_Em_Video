#Formula matematica

catO = float(input('Digite o valor do cateto oposto: '))
catA = float(input('Digite o valor do cateto adjacente: '))
hipot = (catO ** 2 + catA ** 2) ** (1/2)

print(f'O valor da hipotenusa é igual a: {hipot:.2f}')

#Utilizando Bibliotecas

from math import hypot

catO = float(input('Digite o valor do cateto oposto: '))
catA = float(input('Digite o valor do cateto adjacente: '))
hipot = hypot(catO, catA)

print(f'O valor da hipotenusa é igual a: {hipot:.2f}')
