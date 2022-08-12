# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de
# um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

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

def leiaFloat(msg):
    while True:
        n = str(input(msg)).strip()

        try:
            n = float(n)
        except ValueError:
            print('ERRO! Insira um número inteiro!')
        else:
            break
    return n

n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou {n}.')

r = leiaFloat('Digite um número flutuante: ')
print(f'Você digitou {r}.')
