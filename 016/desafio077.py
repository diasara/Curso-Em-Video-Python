# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'python')

for c in range (0, len(palavras)):
  print('\nA palavra {} possui as vogais:' .format(palavras[c]), end = ' ')

  temp = palavras[c]

  for r in range(0, len(temp)):
    if temp[r] in 'aeiou':
      print(temp[r], end = ' ')

'''Professor:

for p in palavras:
  print(f'Na palavra {p} temos ', end = ' ')
  
  for letra in p:
    if letra.lower() in 'aeiou':
      print(letra, end = ' ')

'''
      
print('\n')