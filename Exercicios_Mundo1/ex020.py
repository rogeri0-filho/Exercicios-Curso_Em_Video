from time import sleep

nome = str(input('Digite seu nome completo: ')).strip()


print('ANALISANDO SEU NOME...')
sleep(1)

print(f'Seu nome em maiusculo é: {nome.upper()}!')
print(f'Seu nome em minusculo é: {nome.lower()}!')
print(f'A quantidade de letras é: {len(nome) - nome.count(" ")}!')
print(f'Já seu primeito nome tem {nome.find(" ")} letras!')


