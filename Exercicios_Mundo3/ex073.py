valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o ultimo número: ')),)

print(f'Voce digitou os valores {valores}.')
print(f'O número 9 apareceu {valores.count(9)} vezes.')

if 3 in valores:
    print(f'O número 3 foi digitado na {valores.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')

print('Os valores pares digitados foram', end='')

for c in valores:
    if valores % 2 == 0:
        print(c, end=' ')
