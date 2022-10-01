from lib.intarface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Programa'])
    if resposta == 1:
       lerArquivo(arq)
       
    if resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = readInt(input('Idade: '))
        cadastrar(arq, nome, idade)
        
    elif resposta == 3:
        cabeçalho('Saindo do Programa... Até Logo!!!')
        break
    else:
        print('\033[0;31mERRO!! Digite um valor válido.\033[m')
    sleep(1.5)
