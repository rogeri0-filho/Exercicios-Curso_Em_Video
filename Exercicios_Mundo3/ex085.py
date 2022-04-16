matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #matriz 3x3
#declarando a matriz dessa forma, variavel.append() se torna irrelevante

somapar = somacoluna = maior = 0
for linha in range(0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f'Insira um valor para lxc: [{linha}, {coluna}]'))
        #estrutura  que vai inserir os dados na matrix 3x3

print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')

        if matriz[linha][coluna] % 2 == 0: #verifica os elemtnos pares na matriz
            somapar += matriz[linha][coluna] #faz a soma dos elementos

    print() #quando a contagem de colunas acaba, uma linha é quebrada
    #estrutura que vai organizar os dados na matriz

print('-=' * 30)
print(f'A soma dos valores pares é: {somapar}!')

for linha in range(0, 3):
    somacoluna += matriz[linha][2]
'''
Como os elementos da terceira coluna estao fixos na posição 2, 
só é necessário varrer os elementos da linha [0, 2],[1, 2] e [2, 2], já que são
os únicos elementos que se alteram. No fim, os elementos da 3ª linha são somados.
'''
print(f'A soma dos elementos da 3ª coluna é: {somacoluna}!')

for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
'''
Como o elemento da linha esta fixo no valor 1, segue a mesma logica do for passado
mas, nesse caso, é verificado qual o maior elemento da 2ª linha. 
'''
print(f'O maior valor da 2ª linha é: {maior}!')
print('--' * 30)
