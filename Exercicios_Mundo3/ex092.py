dados = dict()
lista = list()
soma = media = 0 #vai calcular a media das idades

#Input de dados
while True:
    dados.clear() #limpa os valores no dicionário antes de tudo
    dados['Nome'] = str(input('Nome: '))

    while True: #Verifica as respostas e trata os erros de [M/F]
        dados['Sexo'] = str(input('Sexo [M/F]:')).upper()[0]
        if dados['Sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M ou F.')

    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']

    lista.append(dados.copy()) #Adiciona a lista, uma copia do dicionário

    while True: #Verifica as respostas e trata os erros de [S/N]
        resposta = str(input('Deseja continuar? [S/N]:')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break

print('=+=' * 20)

print(f'(A) Ao todo {len(lista)} pessoas foram cadastradas.')

media = soma / len(lista)

print(f'(B) A media das idades é de: {media:.1f} anos')
print('(C) As mulheres cadastradas foram: ', end='')

for c in lista:
    if c['Sexo'] == 'F':
        print(f'{c["Nome"]} ', end='')
print()

print('(D) A lista de pessoas que estão a cima da média: ', end='')
for p in lista:
    if p['Idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
        
print('<<< ENCERRADO >>>')
