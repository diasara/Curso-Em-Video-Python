# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# 	a) Qual é o total gasto na compra.
# 	b) Quantos produtos custam mais de R$ 1000,00.
# 	c) Qual é o nome do produto mais barato.

total = count = count1000 = 0

while True:
  nome = str(input('\nQual o nome do produto? '))
  preco = float(input('\nQual o preço do produto? '))
  
  total += preco 
  
  if preco > 1000: count1000 += 1
  
  if count == 0:
    nomeMaisBarato = nome
    maisBarato = preco
  elif preco < maisBarato:
    nomeMaisBarato = nome
    maisBarato = preco

  count += 1

  opcao = ' '

  while opcao not in 'SN':
    opcao = str(input('\nVocê quer continuar? [S/N]\n')).upper()[0]
  
  if opcao == 'N':
    break

print(f'''O total gasto é de R$ {total:.2f}.
{count1000} produtos custam mais de R$ 1000.00.
{nomeMaisBarato} foi o produto mais barato da compra.\n''')
