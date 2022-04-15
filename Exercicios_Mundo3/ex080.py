lista = list()
lpares = list()
limpares = list()

while True:
    lista.append(int(input("Digite um valor para armazena-lo na lista: ")))
    resposta = str(input('Deseja continuar [S/N]:')).upper()
    if resposta == 'N':
        break

for indice, val in enumerate(lista):
    if val % 2 == 0:
        lpares.append(val)
    elif val % 2 == 1:
        limpares.append(val)

print('-~-' * 30)
print(f'A lista completa de números é: {lista}!')
print(f'A lista de números pares é: {lpares}!')
print(f'A lista de números impares é: {limpares}!')
print('-~-' * 30)
