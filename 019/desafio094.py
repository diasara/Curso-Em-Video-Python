# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#   A) Quantas pessoas foram cadastradas.
#   B) A média de idade do grupo.
#   C) Uma lista com todas as mulheres.
#   D) Uma lista com todas as pessoas com idade acima da média. '''

dict = {}
list = []

while True:
  dict['Nome'] = str(input('\nNome: ')).strip().title()
  dict['Sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
  dict['Idade'] = int(input('Idade: '))

  list.append(dict.copy())

  decisao = ' '

  while decisao not in 'SN':
    decisao = str(input('Quer continuar[S/N]? ')).strip().upper()[0]

  if decisao == 'N':
    break

print(f'\nForam registradas {len(list)} pessoas.')

somatorio_idade = 0
for c in range(0, len(list)):
  somatorio_idade += list[c]['Idade']

media_idade = somatorio_idade / len(list)

print(f'A média de idade é de {media_idade:.2f}.')

print('\nAs mulheres do grupo:')
for c in range(0, len(list)):
  if list[c]['Sexo'] == 'F':
    print(list[c]['Nome'])

print('\nPessoas acima da média de idade:')
for c in range(0, len(list)):  
  if list[c]['Idade'] > media_idade:
    print(list[c]['Nome'])

# Pouquissímas diferentes entre o meu código e o código do
# professor. A maior é em relação ao for.
