def intrtHelp(cmd):
    help(cmd)


comando = ''

while True:
    comando = str(input('Função-Lib-Método [Fim - para] -> '))
    if comando.upper()[0] == 'F':
        break
    else:
        intrtHelp(comando)
