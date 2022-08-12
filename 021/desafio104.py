# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à
# função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

# Ex.:
# n = leiaInt('Digite um n')

def leiaInt(msg):
    while True:
        n = str(input(msg)).strip()

        if n.isdigit():
            break
        else:
            print('ERRO! Insira um número inteiro!')
    
    return int(n)

n = leiaInt('Digite um número: ')

print(f'Você digitou {n}.')
        