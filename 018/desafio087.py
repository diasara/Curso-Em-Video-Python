# Aprimore o desafio anterior, mostrando no final:
# 	a) A soma de todos os valores pares digitados.
# 	b) A soma dos valores da terceira coluna.
# 	c) O maior valor da segunda linha.

matriz = []
dados = []
count = 1
somaPar = soma3 = maior2 = 0

# c é as linhas
for c in range(0, 3):
  # r é as colunas
  for r in range(0, 3):
    dados.append(int(input(f'Digite o {count}° valor: ')))
    count += 1
    
    if dados[r] % 2 == 0:
      somaPar += dados[r]

    if r == 2:
      soma3 += dados[r]

  matriz.append(dados[:])

  if c == 1:
    maior2 = max(dados)

  dados.clear()

print()

for c in range(0, 3):
  print(matriz[c])

print(f'\nA soma dos valores pares é {somaPar}.')
print(f'A soma dos valores da terceira coluna é {soma3}.')
print(f'O maior valor da segunda linha é {maior2}.')

# A resolução do professor é parecida com a minha, então não me dei o trabalho de copiar.
