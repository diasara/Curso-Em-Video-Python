# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = count = 0

while True:
  n = int(input('Digite um número a ser somado(999 para parar): '))

  if n == 999: break
  
  soma += n
  count += 1

print(f'\nA soma dos números é {soma}. Foram digitados {count} números.')
