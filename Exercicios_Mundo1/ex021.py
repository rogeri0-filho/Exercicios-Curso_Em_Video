from time import sleep

valor = int(input('Digite um numero de 0 a 9999: '))

u = valor // 1    % 10
d = valor // 10   % 10
c = valor // 100  % 10
m = valor // 1000 % 10

print('Analisando valor digitado...')
sleep(1)

print(f'A unidade vale: {u}')
print(f'A dezena vale: {d}')
print(f'A centena vale: {c}')
print(f'O milhar vale: {m}')
