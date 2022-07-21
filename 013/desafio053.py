#  Crie um programa que leia uma frase qualquer e diga 
# se ela é um palíndromo, desconsiderando os espaços.

n = str(input('Digite a string: ')).upper().split()

n = ''.join(n)

count = 0

for c in range(0, len(n) // 2):      # Dá pra escrever desse modo "inverso = n[::-1]" para encontrar o inverso da string.
  if n[c] != n[len(n) - 1 - c]:
    count += 1

if count == 0:
  print('É um palíndromo!')
else:
  print('Não é um palíndromo!')
