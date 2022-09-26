import conversor

p = float(input('Digite um valor R$'))
print(f' A Metade de R${p} é {conversor.metade(p, True)}')
print(f' O Dobro de R${p} é {conversor.dobro(p, True)}')
print(f' O Valor R${p} com desconto de 10% é {conversor.desconto(p, 10, True)}')
print(f' O Valor R${p} com acrescimo de 10% é {conversor.acrescimo(p, 10, True)}')
