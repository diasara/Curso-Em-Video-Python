# Faça um prorama que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for c in range(0, 5):
  lista.append(int(input(f'Digite um valor para a posição {c}: ')))

menor = min(lista)
maior = max(lista)

listaMaiores = []
listaMenores = []

# Os dois if's precisam acontecer para caso o usuário digite o mesmo número todas as vezes.
for c in range(0, 5):
  if lista[c] == maior:
    listaMaiores.append(c)

  if lista[c] == menor:
    listaMenores.append(c)

'''Professor:

for i, v in enumerate(lista):
  if v == maior:
    print(f'{i}...', end = '')

for i, v in enumerate(lista):
  if v == menor:
    print(f'{i}...', end = '')

Nesse caso, teria que colocar o for depois de cada print. Achei a minha versão mais organizada.
'''
  
print(f'\nO maior valor é {maior} e está nas posições: ', listaMaiores)
print(f'O menor valor é {menor} e está nas posições: ', listaMenores)
