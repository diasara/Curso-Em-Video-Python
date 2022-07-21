# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
#  pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

from statistics import median

lista = []
listaImpares = []
listaPares = []

while True:
  n = int(input('\nDigite um número: '))

  lista.append(n)

  if n % 2 == 0:
    listaPares.append(n)
  else:
    listaImpares.append(n)
  
  decisao = ' '

  while decisao not in 'SN':
    decisao = str(input('\nVocê quer continuar [S/N]? ')).upper()[0]

  if decisao == 'N':
    break

print('\nLista = ', lista)
print('Lista dos valores ímpares = ', sorted(listaImpares))
print('Lista dos valores pares = ', sorted(listaPares))
