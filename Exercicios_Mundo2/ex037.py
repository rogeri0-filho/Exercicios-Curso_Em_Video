from datetime import date

print('\033[1;32m=\033[1;33m+\033[m' * 12)
print('\033[1;33;4m ALISTAMENTO MILITAR!\033[m')
print('\033[1;32m=\033[1;33m+\033[m' * 12)

ano = int(input('\033[4mDigite o seu ano de nascimento\033[m: '))
idade = (date.today().year - ano)
print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}!')

if idade == 18:
    print('Você já tem a idade necessária para se alistar!')
elif idade > 18:
    print(f'Você deveria ter se alistado a {idade - 18} anos atrás!')
    print('Procure o local de alistamento mais próximo e aliste-se IMEDIATAMENTE!!')
elif idade < 18:
    print(f'Ainda faltam {(idade - 18) * (-1)} anos para o seu alistamento.')
    print(f'Seu alistamento será em {date.today().year + (18 - idade)}')
