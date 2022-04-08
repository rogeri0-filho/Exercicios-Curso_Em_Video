from time import sleep

d = float(input('Digite a distância da sua viagem: '))

if d <= 200:
    p = (d * 0.50)
    print(f'Você acaba de iniciar uma viagem de {d}KM!')
    print('Calculando o valor da sua passagem...')
    sleep(2)
    print(f'O valor da sua passagem é R${p:.2f}!')
else:
    p2 = (d * 0.45)
    print('Você acaba de iniciar uma viagem com mais de 200KM!')
    print('Calculando o valor da sua passagem...')
    sleep(2)
    print(f'O valor da sua passagem vai ser de R${p2:.2f}!')
