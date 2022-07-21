# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador PERDER, mostrando 
# o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

count = 0

while True:
  computador = randint(1,11)
  
  escolha = str(input('\nImpar ou Par? ')).lower()
  jogada = int(input('Vai jogar qual número? '))

  print(f'\nVocê escolheu {escolha} e jogou {jogada}.')
  print(f'O computador jogou {computador}.\n')

  decisao = (jogada + computador) % 2
  
  if escolha == 'par':
    if decisao == 0:
      print('Você venceu! Tente novamente!')
      count += 1
    else:
      print('Você perdeu!')
      break
  else:
    if decisao != 0:
      print('Você venceu! Tente novamente!')
      count += 1
    else:
      print('Você perdeu!')
      break

print(f'\nVocê venceu {count} vezes consecutivos!')
