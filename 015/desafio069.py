# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário 
# quer ou não continuar. No final mostre:
#   a) Quantas pessoas tem mais de 18 anos.
#   b) Quantos homens foram cadastrados.
#   c) Quantas mulheres tem menos de 20 anos.

count18 = countHomens = countMulheres20 = 0
sexo = parada = ' '

while True:
  idade = int(input('\nQual a sua idade? '))

  while sexo not in 'MF':
    sexo = str(input('\nQual o seu sexo? [M/F]\n')).upper()[0]

  if idade > 18: count18 += 1
  if sexo == 'M': countHomens += 1
  if sexo == 'F' and idade > 20: countMulheres20 += 1

  while parada not in 'SN':
    parada = str(input('\nVocê quer continuar? [S/N]\n')).upper()[0]

  if parada == 'N':
    break

print(f'''\n{count18} pessoas tem mais de 18 anos.
{countHomens} pessoas cadastradas são homens.
{countMulheres20} pessoas são mulheres com mais de 20 anos.''')