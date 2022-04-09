print('*+' * 10)
print('   \033[4mMÉDIA ESCOLAR!\033[m')
print('*+' * 10)

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = ((n1 + n2) / 2)

if media < 5:
    print(f'Sua média é {media:.2f}!')
    print('Você está \033[31;1mREPROVADO!\033[m')

elif 5 <= media <= 6.9:
    print(f'Sua média é {media:.2f}!')
    print('Você está em \033[1;33mRECUPERAÇÃO!!\033[m')

elif media >= 7:
    print(f'Sua média é {media:.2f}!')
    print('Meus parabéns, você foi \033[1;32mAPROVADO!!!\033[m')
