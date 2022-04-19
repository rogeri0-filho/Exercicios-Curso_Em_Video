def readInt(msg):
    verificador = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            verificador = True
        else:
            print('\033[0;31mERRO!! Digite um valor válido.\033[m')
        if verificador:
            break
    return valor


n = readInt('Digite um número qualquer: ')
print(f'Você digitou o número {n}!')
