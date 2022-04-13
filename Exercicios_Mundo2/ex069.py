print('=' * 30)
print(f'{"CAIXA ELETRÔNICO":^30}')
print('=' * 30, ' \n')

valor = int(input('Quanto deseja sacar? R$'))
val = valor
ced = 50
totced = 0

while True:
    if val >= ced:
        val -= ced
        totced += 1
        
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
            
        if ced == 50:
            ced = 20
            
        elif ced == 20:
            ced = 10
            
        elif ced == 10:
            ced = 1
        totced = 0
        
        if val == 0:
            break

print('=' * 30)
print('OBRIGADO. Volte Sempre!!!')
