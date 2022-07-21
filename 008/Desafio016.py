# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

num = float(input('Digite um número: '))
print('{}' .format(trunc(num)))

# Dá pra fazer esse exercício sem o uso da biblioteca math.

num2 = float(input('Digite um número: '))
print('{}' .format(int(num2)))