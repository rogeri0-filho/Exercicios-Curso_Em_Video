p = int(input('Primeiro termo: ')) #primeiro termo
r = int(input('Razão: ')) #razão
t = p #recebe o primeiro termo
c = 1 #contador

while c <= 10:
    print(t, end=' ')
    t += r #termo recebe ele mais a razão
    c += 1 #contador recebe ele mais 1
print('FIM!')
