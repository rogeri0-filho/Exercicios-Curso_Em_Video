def notas(*n, sit=False):
    lista_Notas = dict()
    lista_Notas['Total'] = len(n)
    lista_Notas['Maior'] = max(n)
    lista_Notas['Menor'] = min(n)
    lista_Notas['Média'] = sum(n)/len(n)

    if sit:
        if lista_Notas['Média'] >= 6:
            lista_Notas['Situação'] = 'RAZOÁVEL'

        elif lista_Notas['Média'] >= 7:
            lista_Notas['Situação'] = 'BOA'

        elif lista_Notas['Média'] >= 8:
            lista_Notas['Situação'] = 'ÓTIMA'

        else:
            lista_Notas['Situação'] = 'RUIM'

    return lista_Notas


resposta = notas(9, 1, 7, 3, sit=True)
print(resposta)
