def ficha(jogador='<Desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gols!')


jog = str(input('Nome do Jogador: '))
gol = str(input('Nº de Gols: '))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if jog.strip() == '':
    ficha(gols=gol)
else:
    ficha(jog, gol)
