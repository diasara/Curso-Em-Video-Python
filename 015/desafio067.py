# Faça um programa que mostre a tabuada de vários números, um de 
# cada vez, para cada valor digitado pelo usuário. 
# O programa erá interrompido quando o número solicitado for negativo.

print('-' * 20, 'Tabuada', '-' * 20)

while True:
  n = int(input('Digite o número que você quer saber a tabuada: '))

  if n < 0: break

  print('-' * 15,f'Tabuada do {n}', '-' * 15)
  for c in range(1, 11):
    print('{} x {:2} = {}' .format(n, c, n * c))
  print('-' * 50)

print('-' * 20, 'Fim do Programa', '-' * 20)