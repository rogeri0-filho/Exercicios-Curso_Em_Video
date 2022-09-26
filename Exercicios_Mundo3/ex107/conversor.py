def dobro(preço = 0, formatacao = False):
    resposta = preço * 2
    return resposta if formatacao is False else moeda(resposta)
    

def metade(preço = 0, formatacao = False):
    resposta = preço / 2
    return resposta if formatacao is False else moeda(resposta)


def acrescimo(preço = 0, taxa = 0, formatacao = False):
    resposta = preço + (preço * (taxa/100))
    return resposta if formatacao is False else moeda(resposta)
    
    
def desconto(preço = 0, taxa = 0, formatacao = False):
    resposta = preço - (preço * (taxa/100))
    return resposta if formatacao is False else moeda(resposta)


def moeda(preço = 0):
    resposta = str(f'R${preço:.2f}').replace('.', ',') #Subistitui os '.' por ',' como seprarador das casas decimais
    return resposta
    
    