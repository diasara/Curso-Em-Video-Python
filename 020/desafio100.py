# Faça um programa que tenha uma lista chamada números e
# duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a
# segunda função vai mostrar a soma entre todos os valores PARES 
# sorteados pela função anterior.

from random import randint

def sorteia(list):
    for c in range(0, 5):
        list.append(randint(0, 100))

    print('Números sorteados:')
    print(list)

def somaPar(list):
    soma = 0

    for c in range(0, len(list)):
        if list[c] % 2 == 0:
            soma += list[c]

    return soma

lista = []

sorteia(lista)

print(f'A soma dos números pares é {somaPar(lista)}.')
