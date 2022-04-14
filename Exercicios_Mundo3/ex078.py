lista = list()

for contador in range(0, 5):
    entrada = int(input('Insira um valor: '))

    if contador == 0 or entrada > lista[-1]:
        lista.append(entrada)

    else:
        posição = 0

        while posição < len(lista):
            if entrada <= lista[posição]:
                lista.insert(posição, entrada)
                break

            posição += 1
            
print('--' * 30)
print(f'Os valores digitados foram: {lista}!')
