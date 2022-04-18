from datetime import datetime

def voteAnalysis(votar):
    idadeVoto = datetime.now().year - nascimento
    if idadeVoto >= 18:
        return f'Voto Obrigatório. você ja tem {idadeVoto}!!'
    elif 16 <= idadeVoto < 18 or idadeVoto > 65:
        return f'Voto Opocional!!. Você tem {idadeVoto}'
    elif idadeVoto < 16:
        return f'Voto Negado!!. Você tem {idadeVoto}'


nascimento = int(input('Digite seu ano de nascimento: '))
print(voteAnalysis(nascimento))
