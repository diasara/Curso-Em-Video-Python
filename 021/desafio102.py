# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro
# que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show = False):
    from time import sleep

    resp = 1
    for c in range(num, 1, -1):
        resp *= c

        if show:
            print(c, end = ' x ', flush = True)

            sleep(0.5)

            if c - 1 == 1:
                print('1. FIM!')
                break

    print(f'O fatorial de {num} é {resp}.')

n = int(input('Qual o número que você quer saber o fatorial? '))

fatorial(n, False)
