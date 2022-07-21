# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#  A) Quantos números foram digitados.
#  B) A lista de valores, ordenada de forma decrescente.
#  C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
  n = int(input('\nDigite um número: '))

  lista.append(n)

  decisao = ' '

  while decisao not in 'SN':
    decisao = str(input('\nVocê quer continuar [S/N]? ')).upper()[0]

  if decisao == 'N':
    break

print(f'\nForam digitados {len(lista)} números.')

print(sorted(lista, reverse = True))

if 5 in lista:
  print(f'O número 5 está na lista.\n')
else:
  print('O número 5 não apareceu na lista.\n')