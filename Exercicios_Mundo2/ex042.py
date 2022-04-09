print('=$' * 16)
print('   \033[4mGERENCIADOR DE PAGAMENTOS\033[m')
print('=$' * 16)

pagar = float(input('Preço total das compras: R$'))

print('FORMAS DE PAGAMENTO:')
print('[1] à vista dinheiro/cheque\n'
      '[2] à vista cartão\n'
      '[3] 2x cartão\n'
      '[4] 3x ou mais cartão')
opção = int(input('Qual sua opção? '))

if opção == 1:
    print(f'Sua compra de R${pagar} ficará por R${pagar -(pagar * 0.10):.2f}.')

elif opção == 2:
    print(f'Sua compra de R${pagar} ficará por R${pagar -(pagar * 0.05):.2f}.')

elif opção == 3:
    print(f'Sua compra será parcelada em 2x de R${pagar/2:.2f}. SEM JUROS!')

elif opção == 4:
    total = pagar + (pagar * (20/100))
    parctot = int(input('Em quantas vezes deseja parcelar?'))

    parc = total / parctot
    print(f'Sua compra será parcelada em {parctot} de R${parc}. COM JUROS!')
