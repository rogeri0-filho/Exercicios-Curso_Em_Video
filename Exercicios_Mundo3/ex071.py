tupla = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino', 'Athletico-PR', 'Ceará', 'Bahia', 'Fluminense',
         'Flamengo', 'Santos', 'Atlético-GO', 'Corinthians', 'Juventude', 'São Paulo', 'Internacional', 'América-MG',
         'Sport', 'Grêmio', 'Cuiabá', 'Chapecoense')

print('===' * 20)
print(f'{"Tabela do Campeonato Brasileiro de Futebol":^59}')
print('===' * 20)

print('Lista dos times: ', tupla, '\n', '~~~~' * 20)
print('Os 5 primeiros times: ', tupla[:5], '\n', '~~~~' * 20,)
print('Os 4 últimos colocados: ', tupla[-4:], '\n', '~~~~' * 20,)
print('Times em ordem alfabética: ', sorted(tupla), '\n', '~~~~' * 20,)
print('Posição do time Chapecoense: ', tupla.index('Chapecoense')+1)
