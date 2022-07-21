# Faça um programa que leia nome e média de um aluno, guardando também 
# a situação em um dicionário. No final, mostre o conteúdo da estrututra na tela.

dicio = {}
print('-' * 30)
dicio['Nome'] = str(input('Nome: ')).strip().title()
dicio['Média'] = float(input('Média: '))

if dicio['Média'] < 6.0:
  dicio['Situação'] = 'Reprovado'
else:
  dicio['Situação'] = 'Aprovado'

print('-' * 15, 'BOLETIM', '-' * 15)
for k, v in dicio.items():
  print(f'{k} = {v}')
