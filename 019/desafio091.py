# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep

jogadas = {}

for c in range(0, 6):
  jogadas[f'Jogador {c + 1}'] = randint(1, 6)
 
print('-' * 15, 'JOGADAS', '-' * 15)
for k, v in jogadas.items():
  print(f'{k} jogou {v}.')
  sleep(2)

print()
print('-' * 15, 'RANKING', '-' * 15)
for i in sorted(jogadas, key = jogadas.get, reverse = True):
  print(i, jogadas[i])

'''
O professor usou uma função chamada itemgetter pra fazer
a mesma coisa que eu fiz. O que muda é que pra isso, é
necessário criar uma lista porque a função devolve uma
lista.
'''