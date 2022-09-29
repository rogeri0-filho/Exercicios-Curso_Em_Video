def readFloat(msg):
    while True:
        try:
            reader = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!! Digite um valor válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário optou por não informar os dados!\033[m')
            return 0
        else:
            return reader
        