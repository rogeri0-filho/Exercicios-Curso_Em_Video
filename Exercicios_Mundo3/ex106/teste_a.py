import conversoesA

p = float(input('Digite um valor R$'))
print(f' A Metade de R${p} é {conversoesA.moeda(conversoesA.metade(p))}')
print(f' O Dobro de R${p} é {conversoesA.moeda(conversoesA.dobro(p))}')
print(f' O Valor R${p} com desconto de 10% é {conversoesA.moeda(conversoesA.desconto(p, 10))}')
print(f' O Valor R${p} com acrescimo de 10% é {conversoesA.moeda(conversoesA.acrescimo(p, 10))}')
