tuplap = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis')

for c in tuplap:
    print(f'\nNa palavra {c.upper()} temos as vogais: ', end='')
    for letras in c:
        if letras.lower() in 'aáàâãäeéèêëiíìïîoóòôõöuúùü':
            print(letras, end=' ')
