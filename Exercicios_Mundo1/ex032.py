s = float(input('Digite o salário atual do funcionário: R$ '))

if s <= 1250:
    novo = s + (s * (15/100))
    print(f'Com o acrescimo de 15%, o salário do funcionário agora é: R${novo:.2f}')
else:
    novo = s + (s * (10/100))
    print(f'Com o acrescimo de 10%, o salário do funcionário agora é: R${novo:.2f}')
