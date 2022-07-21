# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
  n = int(input('\nDigite um valor: '))

  if n not in lista:
    lista.append(n)
  else:
    print('\nEsse valor já está na lista!')

  decisao = ' '

  while decisao not in 'SN':
    decisao = str(input('\nQuer continuar? [S/N] ')).upper()[0]

  if decisao == 'N':
    break

print('-' * 30)
print(sorted(lista))