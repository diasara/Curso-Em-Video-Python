# Modifique as funções que foram criadas no desafio 107 para que elas
# aceitem um parâmetro a mais, informando se o valor retornado por elas vai 
# ser ou não formatado pela função moeda(), desenvolvido no desafio 108.

import moeda

n = float(input('Digite um número: '))

print(f'O número {moeda.moeda(n)} aumentado em 80% é igual a {moeda.aumentar(n, 80, mon = True)}.')
print(f'O número {moeda.moeda(n)} aumentado em 80% é igual a {moeda.aumentar(n, 80)}.')
print(f'O número {moeda.moeda(n)} diminuído em 80% é igual a {moeda.diminuir(n, 80, mon = True)}.')
print(f'O número {moeda.moeda(n)} diminuído em 80% é igual a {moeda.diminuir(n, 80)}.')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, mon = True)}.')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n)}.')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, mon = True)}.')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n)}.')
