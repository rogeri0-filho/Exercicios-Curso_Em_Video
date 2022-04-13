ttc, ttc2, menor, cont = 0
menorp = ' '

while True:
    print('---' * 20)
    p = str(input('Nome do produto: '))
    v = float(input('Preço: R$'))
    cont += 1
    print('---' * 20)
    c = ' '

    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    ttc += v

    if v >= 1000:
        ttc2 += 1

    if cont == 1:  # if cont == 1 or v < menor:
        menor = v  # menor = v
        menorp = p  # menorp = p

    else:  #
        if v < menor:  # Usando o comando a cima, o else pode ser descartado
            menor = v  # junto com o if dentro dele
            menorp = p  #

    if c == 'N':
        print(f'{" FIM DA COMPRA ":-^40}')
        print(f'O total gasto em compras foi de R${ttc:.2f}.')
        print(f'Ao todo, {ttc2} produtos custaram mais de R$1000,00.')
        print(f'O produto mais barato custou R${menor:.2f} e foi {menorp}.')
        break
