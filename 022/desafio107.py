# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().

# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

n = float(input('Digite um número: '))

print(f'O número {n:.2f} aumentado em 80% é igual a {moeda.aumentar(n, 80):.2f}.')
print(f'O número {n:.2f} diminuído em 80% é igual a {moeda.diminuir(n, 80):.2f}.')
print(f'O dobro de {n:.2f} é {moeda.dobro(n):.2f}.')
print(f'A metade de {n:.2f} é {moeda.metade(n):.2f}.')
