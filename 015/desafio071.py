# Crie um programa que simule o funcionamento de um caixa eletrônico. 
#   No início, pergunte ao usuário qual será o valor a ser sacado 
#   (número inteiro) e o programa vai informar quantas cédulas de cada 
#   valor serão entregues.
#     Obs.: Considere que o caixa possui cédulas de R$50,00, R$20,00, 
#     R$10,00 e R$1,00.'''

divisao = [50, 20, 10, 1]
valor = float(input('Qual o valor a ser sacado? R$ '))

for c in range(0, 4):
  print(f'{(valor // divisao[c]):.0f} notas de R$ {divisao[c]}.00.')
  valor = valor % divisao[c]
  if valor == 0: break
