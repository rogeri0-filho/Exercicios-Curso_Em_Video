print('><'*35)
print('                    ~~Sequência de Fibonacci~~')
print('><'*35)

n = int(input('Quantos termos deseja mostrar? '))
início = 0 # início da sequência
cont = 1 # contador

while n != 0:
    início += cont #início recebe ele mais o contador(sem isso uma sequência de -1 e 1 são printados de acordo com o input do usuário)
    cont = início - cont #contador recebe o início da sequência(0) - ele mesmo(sem isso apenas uma sequências de 1 são printados de acordo com o valor do input do usuário)
    n -= 1 #input do termo recebe ele mesmo menos 1(sem isso o codigo buga totalmente)
    print(cont, end=' ')
