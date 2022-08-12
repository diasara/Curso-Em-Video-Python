# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.request.URLError:
    print('O site do pudim não está acessível!')
else:
    print('O site do pudim está acessível!')
    # print(site.read()) # Lê o conteúdo da página.
