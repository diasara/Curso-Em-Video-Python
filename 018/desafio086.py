# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com os 
# valores lidos pelo teclado. No final, mostre a matriz na tela, com a 
# formatação correta.

matriz = []
dados = []
count = 1

for c in range(0, 3):
  for r in range(0, 3):
    dados.append(int(input(f'Digite o {count}° valor: ')))
    count += 1
  matriz.append(dados[:])

  dados.clear()

print()

for c in range(0, 3):
  print(matriz[c])

'''Professor:

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
  for c in range(0, 3):
    matriz[l][c] = int(input(f'Digite um valor: para [{l}, {c}]: '))

for l in range(0, 3):
  for c in range(0, 3):
    print(f'[{matriz[l][c]:^5}]')
  print() # Necessário para a quebra de linha.

Não é tão diferente da minha. A maior melhora é que não é necessária uma lista auxiliar.
'''