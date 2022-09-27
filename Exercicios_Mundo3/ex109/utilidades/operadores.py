def dobro(preço = 0, formatacao = False):
    resposta = preço * 2
    return resposta if formatacao is False else moeda(resposta)
    

def metade(preço = 0, formatacao = False):
    resposta = preço / 2
    return resposta if formatacao is False else moeda(resposta)


def acrescimo(preço = 0, taxa = 0, formatacao = False):
    resposta = f'R${preço + (preço * (taxa/100)):.2f}'.replace('.', ',')
    return resposta if formatacao is False else moeda(resposta)
    
    
def desconto(preço = 0, taxa = 0, formatacao = False):
    resposta = f'R${preço - (preço * (taxa/100)):.2f}'.replace('.', ',')
    return resposta if formatacao is False else moeda(resposta)


def moeda(preço = 0):
    resposta = f'R${preço:.2f}'.replace('.', ',') #Subistitui os '.' por ',' como seprarador das casas decimais
    return resposta
    
    
def resumo(preço = 0, taxa_aument = 10, taxa_redu = 5):
    print('-' * 30)
    print('RESUMO DA CONVERSÃO'.center(30))
    print('-' * 30)
    print(f'Valor Analisado: \t{moeda(preço)}')
    print(f'Dobro do Valor: \t{dobro(preço, True)}')
    print(f'Metade do Valor: \t{metade(preço, True)}')
    print(f'Acrscimo (10%-padrão): \t{acrescimo(preço, True)}')
    print(f'Desconto (5%-padrão): \t{desconto(preço, True)}')
    print('-' * 30)
    