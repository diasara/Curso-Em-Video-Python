# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o
# maior valor que estão na tupla.

from random import randint

tupla = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))

for c in range(0, 5):
  print(f'{c + 1}° número = {tupla[c]}')
  
  if c == 0:
    menor = maior = tupla[c]
  else:
    if tupla[c] < menor:
      menor = tupla[c]
    elif tupla[c] > maior:
      maior = tupla[c]

print(f'\nO menor valor da tupla é {menor}, e o maior valor é {maior}.')
