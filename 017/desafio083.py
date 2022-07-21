# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite a expressão: '))

'''Professor:

pilha = []

for simb in expressao:
  if simb == '(':
    pilha.append('(')
  elif simb == ')':
    if len(pilha) > 0:
      pilha.pop()
    else:
      pulha.append(')')
      break

if len(pilha) == 0:
  print('Sua expressão é válida!)
else:
  print('Sua expressão é inválida!')
'''

count = 0

for c in range(0, len(expressao)):  
  if expressao[c] == '(':
    count += 1

  if expressao[c] == ')':
    count -= 1

  if count < 0:
    break

if count == 0:
  print('\nA expressão está correta!\n')
else:
  print('\nA expressão está errada!\n')

# A minha versão é evidentemente mais simples, mas eu 
# não usei listas que é o assunto dessa aula. De todo 
# modo, a ideia é a mesma.
