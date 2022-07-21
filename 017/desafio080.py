# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []

for c in range(0, 5):
  n = int(input(f'Digite o {c + 1}° valor: '))

  if c == 0:
    lista.append(n)
  else:
    for r in range(0, len(lista)):
      if n < lista[r]:
        lista.insert(r, n)

      if r + 1 == len(lista):
        lista.append(n)

'''Professor

for c in range(0, 5):
  n = int(input('Digite um valor: '))
  if c == 0 or n > lista[-1]:
    lista.append(n)
    print('Adicionando ao final da lista...')
  else:
    pos = 0
    while pos < len(lista):
      if n <= lista[pos]:
        lista.insert(pos, n)
        print(f'Adicionando na posição {pos} da lista...')
        break
      pos += 1

Não acho que os códigos sejam diferentes. Eles devem custar o mesmo processamento.
'''

print('-' * 30)
print(lista)