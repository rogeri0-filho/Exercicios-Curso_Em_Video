def dobro(preço = 0):
    resposta = preço * 2
    return resposta
    

def metade(preço = 0):
    resposta = preço / 2
    return resposta


def acrescimo(preço = 0, taxa = 0):
    resposta = preço + (preço * (taxa/100))
    return resposta
    
    
def desconto(preço = 0, taxa = 0):
    resposta = preço - (preço * (taxa/100))
    return resposta


def moeda(preço = 0):
    resposta = str(f'R${preço:.2f}').replace('.', ',') #Subistitui os '.' por ',' como seprarador das casas decimais
    return resposta
    
    