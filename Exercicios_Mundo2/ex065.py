print('=-=' * 20)
print(f'{"TABUADA V3.0":^57}')
print('=-=' * 20)

while True:
 n = int(input('Digite um valor para ver sua tabuada: '))
 if n < 0:
     break
 print('-' * 15)
 for c in range (1, 11):
     print(f'{n} x {c} = {n * c}')
 print('-' * 15)

print('FIM DA TABUADA!')
