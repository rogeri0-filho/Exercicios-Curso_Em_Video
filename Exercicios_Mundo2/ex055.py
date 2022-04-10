sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]

while sexo != 'M' and sexo != 'F':
    print('Dado inválido, ', end='')
    sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]

print(f'Sexo registrado como {sexo}!')
