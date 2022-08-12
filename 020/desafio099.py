# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.

# Seu programa tem que analisar todos os valores e dizer
# qual deles é o maior.



def maior(* num):
    for c, v in enumerate(num):
        if c == 0:
            maior = num[c]
        elif num[c] > maior:
            maior = num[c]

    print(f'O maior número foi {maior}.')

numeros = []

print('Digite quantos números quiser!')

while True:
    n = int(input('Digite um número: '))
    numeros.append(n)

    decisao = ' '

    while decisao not in 'SsNn':
        decisao = str(input('Quer continuar [S/N]? ')).strip()[0]

    if decisao in 'Nn':
        break

maior(* numeros)
