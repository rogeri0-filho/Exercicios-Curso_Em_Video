import conversoes

p = float(input('Digite um valor R$:'))
print(f' A Metade de {p} é {conversoes.metade(p)}')
print(f' O Dobro de {p} é {conversoes.dobro(p)}')
print(f' O Valor {p} com desconto de 10% é {conversoes.desconto(p, 10)}')
print(f' O Valor {p} com acrescimo de 10% é {conversoes.acrescimo(p, 10)}')
