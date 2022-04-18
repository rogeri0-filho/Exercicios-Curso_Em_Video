from time import sleep

def contador(i, f, p):
    '''
    for c in range(i, f, p):
        print(f'{c}', end=' ')
        sleep(0.5)

    print('FIM!')
    '''

    if p < 0:
        p *= -1 #evita que o programa entre em lopp infinito caso o passo seja negativo
    if p == 0:
        p = 1

    print('--' * 20)
    print(f'Contagem de {i} -> {f} de {p} em {p}')

    if i < f: #verifica o contador(1, 10, 1)
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('FIM!')

    else: # verifica o contador(10, 0, 2)
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('Contagem Personalizada')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passos = int(input('Passos: '))

contador(inicio, fim, passos)



#flush=True desliga o buffer de tela