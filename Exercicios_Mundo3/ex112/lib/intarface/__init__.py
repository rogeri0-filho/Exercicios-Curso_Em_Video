def readInt(msg):
    while True:
        try:
            reader = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!! Digite um valor válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário optou por não informar os dados!\033[m')
            return 0
        else:
            return reader
        

def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = readInt('\033[32mSua opção: \033[m')
    return opc

