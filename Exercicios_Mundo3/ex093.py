jogos = dict()
partidas = list()
time = list()

#-------------------------------------------------------------------
#Todo código a baixo, apenas recebe os dados dos jogadores e partididas e verifica as respostas
while True:
    jogos.clear()
    jogos['Nome'] = str(input('Qual o nome do jogador: '))
    totalp = int(input('Quantas partidas jogadas:'))
    partidas.clear()
    for c in range(totalp):
        partidas.append(int(input(f'  -Quantos gols na {c +1}ª partida? ')))

    jogos['Partidas'] = totalp
    jogos['Gols'] = partidas[:]
    jogos['Total'] = sum(partidas)#soma automaticamente, todos os valores dentro de partidas :\

    time.append(jogos.copy())

    while True: #Verifica as respostas e trata os erros de [S/N]
        resposta = str(input('Deseja continuar? [S/N]:')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break

#------------------------------------------------------------------
#Todo o código a baixo, organiza os rezultados em uma tabela
print('---' * 30)

print('Cod:', end='')

for i in jogos.keys():
    print(f'{i:<15}', end='')

print()

print('=+=' * 30)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')

    for d in v.values():
        print(f'{str(d):<15}', end='')

    print()

print('=+=' * 30)
#-------------------------------------------------------------------
#Todo código a partir daqui, é onde é feita a busca pelos dados do jogador e partida
while True:
    busca = int(input('Qual jogador você deseja ver os dados? (999 Break):'))

    if busca == 999:
        break

    if busca >= len(time):
        print(f'ERRO! Não exite jogador com o código: {busca}!')

    else:
        print(f' --LEVANTAMENTO DO JOGADOR ({time[busca]["Nome"]}): ')

        for i, g in enumerate(time[busca]["Gols"]):
            print(f'  -NO jogo {i+1} fez {g} gols!')

    print('-~-' * 30)

print('<<<<VOLTE SEMPRE>>>>')
