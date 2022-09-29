from leitor_numerico import LeitorInteiro
from leitor_numerico import LeitorReal

n1 = LeitorInteiro.readInt(('Digite um número interiro qualquer: '))
n2 = LeitorReal.readFloat(('Digite um número real qualquer: '))
print(f'Você digitou o número inteiro: {n1}!')
print(f'Você digitou o número real: {n2}!')