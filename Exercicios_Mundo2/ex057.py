v1 = float(input('Digite o 1º valor: '))
v2 = float(input('Digite o 2º valor: '))
op = 0

while op != 10:
    print('=-=' * 20)
    print('O que deseja fazer:\n'
          '    [ 1 ] Somar\n'
          '    [ 2 ] Subtrair\n'
          '    [ 3 ] Multiplicar\n'
          '    [ 4 ] Dividir\n'
          '    [ 5 ] Divisão inteira\n'
          '    [ 6 ] Resto da Divisão\n'
          '    [ 7 ] Exponenciar\n'
          '    [ 8 ] Raiz\n'
          '    [ 9 ] Novo número\n'
          '    [ 10 ] Sair do programa')
    print('=-=' * 20)
    op = int(input('>>>> Qual sua opção? '))

    if op == 1:
        r = v1 + v2
        print(f'A Soma entre {v1} e {v2} é igual a {r}!')
    elif op == 2:
        r = v1 - v2
        print(f'A Subtração entre {v1} e {v2} é igual a {r}!')
    elif op == 3:
        r = v1 * v2
        print(f'A Multiplicação entre {v1} e {v2} é igual a {r}!')
    elif op == 4:
        r = v1 / v2
        print(f'A Divisão entre {v1} e {v2} é igual a {r}!')
    elif op == 5:
        r = v1 // v2
        print(f'A Divisão Inteira entre {v1} e {v2} é igual a {r}!')
    elif op == 6:
        r = v1 % v2
        print(f'O Resto da Divisão entre {v1} e {v2} é igual a {r}!')
    elif op == 7:
        ex = int(input('Qual o valor do expoente? '))
        ba = int(input('Qual base deseja exponenciar? '))
        if ex == 1:
            if ba == 1:
                print(f'{v1} elevado a {ex} é igual a {v1 ** 1}!')
            elif ba == 2:
                print(f'{v2} elevado a {ex} é igual a {v2 ** 1}!')
        elif ex == 2:
            if ba == 1:
                print(f'{v1} elevado a {ex} é igual a {v1 ** 2}!')
            elif ba == 2:
                print(f'{v2} elevado a {ex} é igual a {v2 ** 2}!')
        elif ex == 3:
            if ba == 1:
                print(f'{v1} elevado a {ex} é igual a {v1 ** 3}!')
            elif ba == 2:
                print(f'{v2} elevado a {ex} é igual a {v2 ** 3}!')
    elif op == 8:
        r = int(input('Qual o valor da raiz? '))
        ba = int(input('Qual base deseja selecionar? '))
        if r == 2:
            if ba == 1:
                print(f'A raiz {r} de {v1} é igual a {v1 ** (1/2)}!')
            elif ba == 2:
                print(f'A raiz {r} de {v2} é igual a {v2 ** (1/2)}!')
        elif r == 3:
            if ba == 1:
                print(f'A raiz {r} de {v1} é igual a {v1 ** (1/3)}!')
            elif ba == 2:
                print(f'A raiz {r} de {v2} é igual a {v2 ** (1/3)}!')
    elif op == 9:
        print('Quais números deseja adicionar?')
        v3 = float(input('Primeiro novo valor: '))
        v4 = float(input('Segundo novo valor: '))
        if op == 1:
            r = v3 + v4
            print(f'A Soma entre {v3} e {v4} é igual a {r}!')
        elif op == 2:
            r = v3 - v4
            print(f'A Subtração entre {v3} e {v4} é igual a {r}!')
        elif op == 3:
            r = v3 * v4
            print(f'A Multiplicação entre {v3} e {v4} é igual a {r}!')
        elif op == 4:
            r = v3 / v4
            print(f'A Divisão entre {v3} e {v4} é igual a {r}!')
        elif op == 5:
            r = v3 // v4
            print(f'A Divisão Inteira entre {v3} e {v4} é igual a {r}!')
        elif op == 6:
            r = v1 % v2
            print(f'O Resto da Divisão entre {v3} e {v4} é igual a {r}!')
        elif op == 7:
            ex = int(input('Qual o valor do expoente? '))
            ba = int(input('Qual base deseja exponenciar? '))
            if ex == 1:
                if ba == 1:
                    print(f'{v3} elevado a {ex} é igual a {v3 ** 1}!')
                elif ba == 2:
                    print(f'{v4} elevado a {ex} é igual a {v4 ** 1}!')
            elif ex == 2:
                if ba == 1:
                    print(f'{v3} elevado a {ex} é igual a {v3 ** 2}!')
                elif ba == 2:
                    print(f'{v4} elevado a {ex} é igual a {v4 ** 2}!')
            elif ex == 3:
                if ba == 1:
                    print(f'{v3} elevado a {ex} é igual a {v3 ** 3}!')
                elif ba == 2:
                    print(f'{v4} elevado a {ex} é igual a {v4 ** 3}!')
        elif op == 8:
            r = int(input('Qual o valor da raiz? '))
            ba = int(input('Qual base deseja selecionar? '))
            if r == 2:
                if ba == 1:
                    print(f'A raiz {r} de {v3} é igual a {v3 ** (1 / 2)}!')
                elif ba == 2:
                    print(f'A raiz {r} de {v4} é igual a {v4 ** (1 / 2)}!')
            elif r == 3:
                if ba == 1:
                    print(f'A raiz {r} de {v3} é igual a {v4 ** (1 / 3)}!')
                elif ba == 2:
                    print(f'A raiz {r} de {v4} é igual a {v4 ** (1 / 3)}!')
    elif op == 10:
        print('Fim do Programa!!!')
    else:
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE!!!')
