from datetime import date

atual = date.today().year
tmaior = 0
tmenor = 0

for c in range(1, 8):
    nasc = int(input('Digite o seu ano de nascimento: '))
    idade = (atual - nasc)

    if idade >= 21:
        tmaior += 1

    else:
        tmenor += 1

print(f'Ao todo {tmaior} pessoas são MAIORES de idade!\n'
      f'E ao todo {tmenor} pessoas são MENORES de idade!')
