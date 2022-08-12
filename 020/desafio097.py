# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.

def escreva(msg):
    print((len(msg) + 4) * '-')
    print(' ', msg, ' ')
    print((len(msg) + 4) * '-')


msg = str(input('Escreva uma mensagem: '))

escreva(msg)
