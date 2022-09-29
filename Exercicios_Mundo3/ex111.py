import urllib
import urllib.request

try:
    verificar_site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.request.URLError:
    print('O site "http://www.pudim.com.br" não está acessível no momento')
else:
    print('O site "http://www.pudim.com.br" foi aberto com sucesso!')
