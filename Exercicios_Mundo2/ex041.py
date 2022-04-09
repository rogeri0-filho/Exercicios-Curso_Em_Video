from time import sleep

print('\033[1m"\033[m' * 20)
print('   \033[1;4mANÁLISADOR IMC\033[m')
print('\033[1m"\033[m' * 20)

peso = float(input('Qual o seu peso? Kg'))
altura = float(input('Qual sua altura? M'))
imc = peso / altura ** 2

print('Calculando seu IMC...')
sleep(3)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}. Você está ABAIXO DO PESO!')
elif 18.5 <= imc <25:
    print(f'Seu IMC é de {imc:.1f}. Você está com PESO IDEAL!')
elif 25 <= imc < 30:
    print(f'Seu IMC é de {imc:.1f}. Você está com SOBREPESO!')
elif 30 <= imc < 40:
    print(f'Seu IMC é de {imc:.1f}. Você está sofrendo de OBESIDADE!')
else:
    print(f'Seu IMC é de {imc:.1f}. Você está com OBESIDADE MÓRBIDA!\nProcure ajuda o quanto antes!')
