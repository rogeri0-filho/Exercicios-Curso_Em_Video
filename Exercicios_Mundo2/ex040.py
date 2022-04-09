print('\033[1m<>\033[m' * 16)
print('   \033[1;4mANALISADOR DE TRIÂNGULOS\033[m')
print('\033[1m<>\033[m' * 16)

s1 = float(input('Digite o valor do primeiro segmento: '))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos de reta acima formam um triângulo ', end='')

    if s1 == s2 == s3:
        print('EQUILÁTERO!')

    elif s1 != s2 != s3 != s1:
        print('ESCALENO!')

    else:
        print('ISÓSCELES!')

else:
    print('Os segmentos de reta não formam um triângulo!')
 
