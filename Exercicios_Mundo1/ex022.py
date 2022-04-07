cidade = str(input('Digite o nome da sua cidade: ')).upper()
#print(cidade[:5].upper() == 'SANTO') #faz a verificação usando o fatiamento

if 'SANTO' in cidade:
    print('Sua cidade possui a palavra "Santo" em seu nome.')
else:
    print('Sua cidade não possui a palavra "Santo" em seu nome.')
