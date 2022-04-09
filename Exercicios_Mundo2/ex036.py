from time import sleep

print('-' * 21)
print(' COMPÁRADOR NUMÉRICO')
print('-' * 21)

sleep(3)

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

sleep(2)

print('ANALISANDO VALORES...')

if n1 > n2:
    print('O PRIMEIRO valor é maior!')
elif n1 < n2:
    print('O SEGUNDO valor é maior!')
else:
    print('Ambos os valores são IGUAIS!')
