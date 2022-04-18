def maior(*num):
    contador = maior = menor = 0

    print('--' * 20)
    print('Analisando valores passados...')

    for valor in num:
        print(f'{valor} ', end='')

        if contador == 0:
            maior = valor

        else:
            if valor > maior:
                maior = valor

        contador +=1

    print(f'Foram informados {contador} valores!')
    print(f'Dos valores informados, o maior é: {maior}!')
    print('--' * 20)


maior(2, 4, 6, 8, 10)
maior(3, 6, 9, 12)
maior(1, 5, 7, 9)
maior(1)
maior()
