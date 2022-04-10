sidade = 0
midade = 0
mih = 0
nv = ''
tm = 0

for p in range(1, 5):

    print(f'----- {p}ª PESSOA -----')

    nome = str(input('Nome: ')).lstrip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lstrip().upper()

    sidade += idade  # recebe a quantidade de vezes que ela apareceu mais as idades

    if p == 1 and sexo == 'M':
        mih = idade
        nv = nome

    if sexo == 'M' and idade > mih:
        mih = idade
        nv = nome

    if sexo == 'F' and idade < 20:
        tm += 1

midade = sidade / 4

print(f'A média de idade do grupo é: {midade}!')
print(f'O homem mais velho se chama {nv} e tem {mih} anos!')
print(f'Ao todo {tm} tem menos de 20 anos!')
