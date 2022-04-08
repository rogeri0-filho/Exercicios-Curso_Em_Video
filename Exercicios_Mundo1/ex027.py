from time import sleep

v = float(input('Qual sua velocidade atual?'))

if v > 80:
    print('Você está a cima do limite de velocidade permitido!')
    sleep(2)
    print('Você foi multado, reduza a velociade!')
    print('Calculando sua multa...')
    sleep(3)
    multa = (v - 80) * 7
    print(f'Sua multa foi de R${multa:.2f}!')

else:
    print(f'Sua velocidade atual é {v}KM/h! Você está dentro do limite permitido.')
    print('Tenha um Bom Dia!')
