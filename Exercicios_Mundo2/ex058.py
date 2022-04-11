#FORMULA MATEMATICA
from math import factorial
n = int(input('Digite um número: '))
fac = factorial(n)
print(f'O fatorial de {n} é {fac}!')

#CALCULANDO COM LAÇOS
print('=-=' * 20)
print('                  --CÁLCULO FATORIAL--')
print('=-=' * 20)

n = int(input('Qual número você deseja fatorar? '))
c = n
f = 1

while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print(f)
print('Fim da fatoração!')
