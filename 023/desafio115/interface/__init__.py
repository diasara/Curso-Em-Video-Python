def leiaInt(msg):
    while True:
        n = str(input(msg)).strip()

        try:
            n = int(n)
        except ValueError:
            print('ERRO! Insira um número inteiro!')
        else:
            break
    return n

def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt = '0'):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
