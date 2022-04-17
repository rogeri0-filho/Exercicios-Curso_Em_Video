from datetime import datetime

dados = dict()

dados['Nome'] = str(input('Digite seu nome: '))
nascimento = int(input('Em que ano você nasceu: '))

dados['Idade'] = datetime.now().year - nascimento

dados['CTPS'] = int(input('Qual seu carteira de trabalho (0 caso não tenha): '))

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contrato: '))
    dados['Salário'] = float(input('Salário recebido: R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
    #idade + ((ano de contrato + 35) - ano atual)
    #35 representa o tempo de contribuição do funcionário

print('==' * 30)

for k, v in dados.items():
   print(f' -={k} tem o valor {v}')




