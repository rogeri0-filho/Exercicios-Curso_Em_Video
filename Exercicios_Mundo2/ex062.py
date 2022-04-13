n = int(input('Digite um número [999 para parar]: '))
contador = cont = 0

while n != 999:
    cont += 1
    contador = n + contador
    n = int(input('Digite um número [999 para parar]: '))

print(f'Você digitou {cont} números.\nA Soma entre eles vale {contador}!\nFIM DO PROGRAMA!')
