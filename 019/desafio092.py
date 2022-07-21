# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os 
# (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO. 
# O dicionário receberá também o ano de contratação e o salário . 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai ser aposentar. 
# Considere que todo mundo se aposente com 35 anos.'''

from datetime import datetime

disc = {}

disc['Nome'] = str(input('Nome: ')).title()
disc['Ano de Nascimento'] = int(input('Ano de Nascimento: '))
disc['Carteira de Trabalho'] = int(input('Carteira de Trabalho: '))

if disc['Carteira de Trabalho'] != 0:
  disc['Ano de Contratação'] = int(input('Ano de Contratação: '))
  disc['Salário'] = float(input('Salário: '))

  idade = datetime.now().year - disc['Ano de Nascimento']
  aposentadoria_ano =  disc['Ano de Contratação'] + 35
  disc['Aposentadoria aos'] = idade + (aposentadoria_ano - datetime.now().year)
else:
  disc['Ano de Contratação'] = 0
  disc['Salário'] = 0
  disc['Aposentadoria aos'] = 0

print('-' * 15, 'PERFIL', '-' * 15)

for k, v in disc.items():
  print(f'{k}: {v}')

print()