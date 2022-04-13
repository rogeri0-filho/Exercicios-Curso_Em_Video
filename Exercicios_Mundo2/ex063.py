n2 = 'S'
soma = quant = media = maior = menor = 0

while n2 == 'S':

    n = int(input('Digite um número: '))
    n2 = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    soma += n
    quant += 1

    if quant == 1:
        maior = menor = n  # número vai ser o maior e também o menor número pois, por enquanto só existe ele

    else:
        if n > maior:
            maior = n

        if n < menor:
            menor = n

media = soma / quant

print('----' * 20)
print(f'Você digitou {quant} números!\nA soma dos valores digitados é igual a {soma}!')
print(f'E a media desses valores vale {media}!\nJá o maior valor é {maior} e o menor é {menor}!')
print('----' * 20)

print('FIM DO PROGRAMA!')
