# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o
# comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se
# encerrará.

# OBS.: Use cores.

from time import sleep

def escreva(msg):
    print('\033[1;30;44m', end = '')
    print((len(msg) + 4) * '-')
    print(' ', msg, ' ')
    print((len(msg) + 4) * '-')
    print('\033[m', end = '')

while True:
    comando = str(input('Qual comando você tem dúvida? '))

    escreva('Processando...')

    sleep(3)

    if comando.upper() == 'FIM':
        break
    else:
        print('\033[0;30;41m')
        help(comando)
        print(' \033[m')

print('FIM DO PROGRAMA')
