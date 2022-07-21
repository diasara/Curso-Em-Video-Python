# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
#  O programa vai perguntar quantos jogos serão gerados e vai sortear
#  6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

lista = list()
jogo = list()

num = int(input('\nQuantos jogos você irá fazer? '))

for c in range(0, num):
  count = 0
  
  while True:
    num = randint(1, 60)
    if num not in jogo:
      jogo.append(num)
      count += 1
    if count >= 6:
      break
  
  lista.append(jogo[:])

  jogo.clear()

for c in range(0, len(lista)):
  print(f'{c + 1}o. jogo = {lista[c]}')
print()

# O professor não havia dito que era necessário que os números não se repetissem. 
#  Apenas remodelei o código e não achei necessário copiar a versão completa do professor.
