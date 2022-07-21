# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

tupla = (int(input('Digite o primeiro valor: ')), 
         int(input('Digite o segundo valor: ')), 
         int(input('Digite o terceiro valor: ')), 
         int(input('Digite o quarto valor: ')))


print(f'\nO número 9 apareceu {tupla.count(9)} vezes.')

count = 0
for c in range(0, 4):
  if tupla[c] == 3:
    count += 1

if count != 0:
  print(f'O número 3 aparece pela primeira vez na posição {tupla.index(3)}.')
else:
  print('Não existe o número 3 na tupla.')

count = 0

print('Os números pares são:', end = ' ')
for c in range (0, 4):
  if tupla[c] % 2 == 0:
    count += 1
    print(tupla[c], end = ' ')
     
  if c + 1 == 4 and count == 0:
    print('Não há números pares nessa tupla.')

print('\n')
