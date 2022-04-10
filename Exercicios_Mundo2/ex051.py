f = str(input('Digite uma frase: ')).lstrip().upper()
p = f.split()
j = ''.join(p)
i = ''
# i = j[::-1]

for l in range(len(j) - 1, -1, -1):
    i += j[l]

if i == j:
    print('Esta frase É um PALÍNDROMO!')

else:
    print('Esta frase NÃO é um PALÍNDROMO!')
