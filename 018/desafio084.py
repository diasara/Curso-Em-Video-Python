# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#	  a) Quantas pessoas foram cadastradas.
# 	b) Uma listagem com as pessoas mais pesadas.
# 	c) Uma listagem com as pessoas mais leves.

from statistics import median

lista = []
listanumeros = []
dados = []

while True:
  nome = str(input('Digite o nome: ')).title().strip()
  print(nome)
  peso = float(input('Digite o peso: '))
  print(peso)

  dados.append(nome)
  dados.append(peso)
  listanumeros.append(peso)

  print(dados)

  lista.append(dados[:])

  print(lista)

  dados.clear()

  decisao = ' '

  while decisao not in 'SN':
    decisao = str(input('Quer continuar [S/N]? ')).upper().strip()[0]

  if decisao == 'N':
    break

  listaPesados = []
  listaLeves = []

mediana = median(listanumeros)

for c in range(0, len(lista)):
  if lista[c][1] > mediana:
    listaPesados.append(lista[c])
  elif lista[c][1] < mediana:
    listaLeves.append(lista[c])

'''Professor:

while True:
  temp.append(str(input('Nome: ')))
  temp.append(float(input('Peso: ')))
  
if len(princ) == 0:
    mai = men = temp[1]
  else:
    if temp[1] > mai:
      mai = temp[1]
    if temp[1] < men:
      men = temp[1]
  
  princ.append(temp[:])
  temp.clear()
  resp = str(input('Quer continuar? '))
  if resp in 'Nn':
    break

print('-' * 30)
print(f'Os dados foram {princ}')
print(f'O maior peso foi {mai}. Peso de ', end = '')
for p in princ:
  if p[1] == mai:
    print(f'[{p[0]}]', end = '')
print(f'O menor peso foi {men}. Peso de ', end = '')
for p in princ:
    if p[1] == men:
      print(f'[{p[0]}]', end = '') 

Aconteceu um erro de interpretação por minha parte.
'''
  
print(f'\nForam cadastradas {len(lista)} pessoas.')
print(f'As pessoas mais pesadas foram: ', listaPesados)
print(f'As pessoas mais leves foram: ', listaLeves)
  