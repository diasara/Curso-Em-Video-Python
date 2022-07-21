# Crie um programa onde o usuário possa digitar sete valores numéricos 
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

lista = []

count = 0

for c in range(0, 7):
  n = int(input(f'Digite o {c + 1} número: '))

  if c == 0:
    lista.append(n)
  else:
    if n % 2 == 0:
      for r in range(0, len(lista)):      
        if n < lista[r] and lista[r] % 2 == 0:
          lista.insert(r, n)
          break
        elif lista[r] % 2 != 0:
          lista.insert(r, n)
          break
    
    if n % 2 != 0:
      for r in range(0, len(lista)): 
        if n < lista[r] and lista[r] % 2 != 0:
          lista.insert(r, n)
          break
        
print(lista)

'''Professor:

num = [[], []]
valor = 0

for c in range(1, 8):
  valor = int(input('Digite um valor: '))
  if valor % 2 == 0:
    num[0].append(valor)
  else:
    num[1].append(valor)

num[0].sort()
num[1].sort()

print('-=' * 30)
print(f'Os valores pares digitados formam {num[0]}.')
print(f'Os valores pares digitados formam {num[1]}.')

Mais uma vez, houve um erro de interpretação que resultou numa resolução muito mais complicada e demorada.
'''