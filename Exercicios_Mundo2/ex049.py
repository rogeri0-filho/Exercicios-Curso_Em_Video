p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r  # formula matemática

for c in range(p, d + r, r):
    print(f'{c}')

print('ACABOU!')
 
