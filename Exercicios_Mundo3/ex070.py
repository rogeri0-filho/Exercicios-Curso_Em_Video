tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
         'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
         'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Valor inválido, tente novamente. ', end='')

print(f'Você digitou o número {tupla[n]}.')
