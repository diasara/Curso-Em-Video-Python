# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: inicio, fim e passo e realize a contagem.

# Seu programa tem que realizar três contagem atráveis da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada.

from time import sleep

def contador(inicio, fim, passo):
    if inicio > fim:
        fim -= 1
        if passo > 0:
            passo *= -1
    else:
        fim += 1
        if passo < 0:
            passo *= -1

    for c in range(inicio, fim, passo):
        print(c, end = ' ', flush = True)
        sleep(1)
    
    print('\n')


print('Contador de 1 a 10, de 1 em 1:')
contador(1, 10, 1)

print('Contador de 10 até 0, de 2 em 2:')
contador(10, 0, 2)

print('Escolha uma contagem: ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
