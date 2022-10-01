from lib.intarface import *

def arqExiste(nome):
    try:
        a = open(nome, 'rt') #leia um arquivo de texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #escrvaum arquivo de texto, caso não exista, crie um
        a.close()
    except:
        print('Ocorreu um ERRO na criação dor arquivo!')
    else:
        print(f'Arquivo: {nome} foi criado com sucesso!')
        
    
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao tentar ler arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS:')
        print(a.read())
    finally:
        a.close()
        
        
def cadastrar(arq, nome = 'None', idade = 0):
    try:
        a = open(arq, 'at') #colocar coisas dentro do arquivo
    except:
        print('Erro ao tentar ler arquivo!')
    else:
        try:
            a.write(f'{nome} - {idade}\n')
        except:
            print('Erro ao tentar criar arquivo!')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()

