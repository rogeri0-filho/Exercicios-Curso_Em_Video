def dobro(preço):
    resposta = preço * 2
    return resposta
    

def metade(preço):
    resposta = preço / 2
    return resposta

def aumento(preço, taxa):
    resposta = preço + (preço * (taxa/100))
    return resposta
    
def desconto(preço, taxa):
    resposta = preço - (preço * (taxa/100))
    return resposta
