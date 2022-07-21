# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('-' * 30)
print('{:<5}'. format('Listagem de Preços'))
print('-' * 30)

tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00)

for c in range(0, len(tupla), 2):
  print(f'{tupla[c]}', '.' * (20 - len(tupla[c])), f'R$ {tupla[c + 1]:>5.2f}')

'''Professor:

for pos in range(0, len(tupla)):
  if pos % 2 == 0:
    print(f'{tupla[pos]:.<30}', end = ' ')
  else:
    print(f'R$ {tupla[pos]:>7.2f}')

Essa versão é evidentemente mais polida do que a minha.

'''
               
print('-' * 30)