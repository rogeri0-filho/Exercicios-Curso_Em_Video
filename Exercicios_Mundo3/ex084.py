matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #matriz 3x3
#declarando a matriz dessa forma, variavel.append() se torna irrelevante

for linha in range(0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f'Insira um valor para lxc: [{linha}, {coluna}]'))
        #estrutura  que vai inserir os dados na matrix 3x3

print('--' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()#quando a contagem de colunas acaba, uma linha é quebrada
    #estrutura que vai organizar os dados na matriz
