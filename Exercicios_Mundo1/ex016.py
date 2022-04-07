from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do ângulo: '))

sen = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))

print(f'O seno vale: {sen:.2f}')
print(f'O cosseno vale: {coss:.2f}')
print(f'O tangente vale: {tang:.2f}')
