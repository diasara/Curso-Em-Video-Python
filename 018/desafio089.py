# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as 
# notas de cada aluno individualmente. '''

from statistics import mean

lista = list()
boletim = list()

while True:
  nome = str(input('\nNome do aluno: ')).strip().title()
  notas = [float(input('Digite a primeira nota: ')),
         float(input('Digite a segunda nota: '))]
  media = mean(notas)

  boletim.append(nome)
  boletim.append(notas)
  boletim.append(media)

  lista.append(boletim[:])

  boletim.clear()

  decisao = ' '

  while decisao not in 'SN':
    decisao = str(input('\nVocê quer continuar? ')).strip().upper()[0]

  if decisao == 'N':
    break

print('-' * 10 , 'Boletim', '-' * 10)
for c in range(0, len(lista)):
  print(f'{lista[c][0]} - {lista[c][2]}')
print()

print('-' * 10, 'Consulta', '-' * 10)

while True:
  print('De qual aluno você quer ver as notas?')

  for c in range(0, len(lista)):
    print(f'{c} - {lista[c][0]}')
    
  escolha = -1
  
  while True:
    escolha = int(input('\nEscolha: '))

    if 0 <= escolha < len(lista): break

  print(f'\nAs notas de {lista[escolha][0]} são {lista[escolha][1]}.')

  decisao = ' '

  while decisao not in 'SN':
    decisao = str(input('\nVocê quer continuar? ')).strip().upper()[0]

  if decisao == 'N':
    break

print('-' * 10, 'Fim do Programa', '-' * 10)

# A resolução do professor não difere muito da minha. Por isso não copiei.