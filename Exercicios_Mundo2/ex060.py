print('=-=' * 20)
print('                    --GERADOR DE P.A.--')
print('=-=' * 20)

p = int(input('Primeiro termo: '))  # primeiro termo
r = int(input('Razão: '))  # razão

t = p  # recebe o primeiro termo
c = 1  # contador
total = 0  # total de termos que vão ser apresentados
te = 10  # primeiros 10 termos que vão ser mostrados

while te != 0:
    total += te  # total a ser mostrado vai ser o valor total mais a variavel que o usuário desejar

    while c <= total:
        print(t, end=', ')
        t += r  # recebe ele mesmo mais a razão
        c += 1

    print('PAUSA!')
    te = int(input('Quantos termos a mais você deseja mostrar? '))  # termo extra

print(f'Progressão finalizada com {c - 1} termos mostrados!')
print('FIM!!')
