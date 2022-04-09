print('=-=' * 15)
print('           CONVERSOR NUMÉRICO!')
print('=-=' * 15)

n1 = int(input('Digite um número que deseja converter: '))
print('Que tipo de conversão deseja fazer?')
print('Digite:\n[1] para BINÁRIO'
      '\n[2] para OCTAL'
      '\n[3] para HEXADECIMAL')
n2 = int(input('Sua opção: '))

if n2 == 1:
    print(f'O valor em BINÁRIO de {n1} é igual a: {bin(n1)[2:]}!')
elif n2 == 2:
    print(f'O valor em OCTAL de {n1} é igual a: {oct(n1)[2:]}!')
elif n2 == 3:
    print(f'O valor em HEXADECIMAL de {n1} é igual a: {hex(n1)[2:]}!')
else:
    print('OPÇÃO INVÁLIDA!')
 
