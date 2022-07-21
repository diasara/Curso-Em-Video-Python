# Aprimore o desafio 093 para que ele funcione com 
#vários jogadores, incluindo um sistema de visualização 
# de detalhes do aproveitamento de cada jogador.

dict = {}
list = []

while True:
  dict.clear()
  dict['Nome'] = str(input('\nNome: ')).strip().title()
  dict['Número de partidas'] = int(input('Número de partidas: '))

  for c in range(0, dict['Número de partidas']):
    dict[f'Gols na partida {c + 1}'] = int(input(f'Gols na partida {c + 1}: '))
    
  dict['Somatório de gols'] = 0

  for c in range(0, dict['Número de partidas']):
    dict['Somatório de gols'] += dict[f'Gols na partida {c + 1}']

  list.append(dict.copy())
  
  decisao = ' '

  while decisao not in 'SN':
    decisao = str(input('Quer continuar[S/N]? ')).strip().upper()[0]

  if decisao == 'N':
    break

print(list)

while True:
  print()
  print('-' * 15, 'Visualizador', '-' * 15)
  for c in range(0, len(list)):
    print(f'{c} - {list[c]["Nome"]}.')

  while True:
    escolha = int(input('\nQual jogador você quer consultar(Número negativo para parar): '))
    if escolha < len(list):
      break

  if escolha < 0:
    break

  print()
  print('-' * 8, f'Informações do jogador {list[escolha]["Nome"]}', '-' * 8)

  for k, v in list[escolha].items():
    print(f'{k} = {v}.')

# As diferenças no desafio 093 causaram as mesmas
# diferenças no desafio 095. Nada de demais.

# Esses exercícios são bem simples, mas me enrolei porque
# achei que teria que usar dicionário em tudo.
