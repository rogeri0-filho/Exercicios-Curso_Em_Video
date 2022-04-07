real = float(input('Quanto voce tem: R$'))
dolar = float(input('Qual a cotação do dolar: US$'))

print(f'Com R${real:.2f} voce pode comprar US${(real/dolar):.2f}')
