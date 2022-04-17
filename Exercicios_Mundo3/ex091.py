jogos = dict()
partidas = list()

jogos['Nome'] = str(input('Qual o nome do jogador: '))
totalp = int(input('Quantas partidas jogadas:'))

for c in range(totalp):
    partidas.append(int(input(f'Quantos gols na {c +1}ª partida? ')))

jogos['Partidas'] = totalp
jogos['Gols p/ Partida'] = partidas[:]
jogos['Total de Gols'] = sum(partidas)#soma automaticamente, todos os valores dentro de partidas :\

print(jogos)

print('=+=' * 30)

for k, v in jogos.items():
    print(f'O campo {k} tem o valor : {v}!')

print('=+=' * 30)

print(f'O jogador {jogos["Nome"]} jogou {totalp} partidas!')
for k, v in enumerate(jogos['Gols p/ Partida']):
    print(f'    - Na partida {k+1}, fez {v} gols!')
print(f'Foi um total de {sum(partidas)}!')



