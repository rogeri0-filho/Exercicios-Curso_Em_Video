from datetime import date
from time import sleep

print('\033[1;34m~\033[m' * 28)
print('  \033[1;4;36mCLASSIFICAÇÃO DE ATLETAS\033[m')
print('\033[1;34m~\033[m' * 28)

sleep(1.5)

nasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nasc

print('Analisando sua patente...')

sleep(3)

print(f'O atleta tem {idade} anos!')

if idade <= 9:
    print('Sua patente é: MIRIM!')

elif idade <= 14:
    print('Sua patente é: INFANTIL!')

elif idade <= 19:
    print('Sua patente é: JÚNIOR!')

elif idade <= 25:
    print('Sua patente é: SÊNIOR!')

else:
    print('Sua patente é: MASTER!')
 
