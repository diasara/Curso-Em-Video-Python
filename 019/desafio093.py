# Crie um programa que gerencie o aproveitamento de
# um jogador de futebol. O programa vai ler o nome do
# jogador e quantas partidas ele jogou. Depois vai ler a
# quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o 
# total de gols feitos durante o campeonato. '''

dict = {}

dict['Nome'] = str(input('Nome: ')).strip().title()
dict['Número de partidas'] = int(input('Número de partidas: '))

for c in range(0, dict['Número de partidas']):
  dict[f'Gols na partida {c + 1}'] = int(input(f'Gols na paritda {c + 1}: '))

dict['Somatório de gols'] = 0

for c in range(0, dict['Número de partidas']):
  dict['Somatório de gols'] += dict[f'Gols na partida {c + 1}']


print('-' * 15, 'Informações do jogador', '-' * 15)
for k, v in dict.items():
  print(f'{k} = {v}.')


'''
O professor usou lista para agrupar o número de gols e 
usou uma função para o somatório. Tirando algumas
alterações devido a essas diferenças, o código não é
tão diferente do meu.
'''                                           
