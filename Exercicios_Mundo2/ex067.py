from datetime import date

contidade = conthomens = contmulher = 0

while True:
    print('---' * 20)
    i = int(input('Informe sua idade: '))
    s = ' '

    while s not in 'MF':
        s = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
    print('---' * 20)
    conf = ' '

    while conf not in 'SN':
        conf = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    print('~~~' * 20)

    if i >= 18:
        contidade += 1

    if s == 'M':
        conthomens += 1

    if s == 'F':
        if i < 20:
            contmulher += 1
            
    if conf == 'N':
        print('FIM DO PROGRAMA !')
        print(f'{contidade} pessoas tinham mais de 18 anos.')
        print(f'{conthomens} homens foram cadastrados.')
        print(f'{contmulher} mulheres tem menos de 20 anos.')
        print('~~~' * 20)
        break
