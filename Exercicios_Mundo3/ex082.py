lista1 = list()
lista2 = list()
maior = menor = 0

while True:
    lista1.append(str(input('Digite seu nome: ')))
    lista1.append(float(input('Digite seu peso: Kg')))

    if len(lista2) == 0: #guarda o > e < peso junto com a lista[1]
        maior = menor = lista1[1] #lisat1[0] = nome / lista[1] = peso
    else:
        if lista1[1] > maior:
            maior = lista1[1]
        if lista1[1] < menor:
            menor = lista1[1]

    lista2.append(lista1[:])
    lista1.clear()

    resposta = str(input('Deseja continuar [S/N]: ')).upper()
    if resposta == 'N':
        break

print('--' * 30)
print(f'Ao todo, {len(lista2)} pessoas foram cadastradas!')

print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for pessoa in lista2:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}] ', end='')
print()

print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for pessoa2 in lista2:
    if pessoa2[1] == menor:
        print(f'[{pessoa2[0]}] ', end='')
print()
