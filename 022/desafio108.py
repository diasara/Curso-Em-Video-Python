# Adapte o código do desafio 107, criando uma função adicional chamada
# moeda() que consiga mostrar os valores como um valor monetário formatado.

import moeda

n = float(input('Digite um número: '))

print(f'O número {moeda.moeda(n)} aumentado em 80% é igual a {moeda.moeda(moeda.aumentar(n, 80))}.')
print(f'O número {moeda.moeda(n)} diminuído em 80% é igual a {moeda.moeda(moeda.diminuir(n, 80))}.')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}.')
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}.')
