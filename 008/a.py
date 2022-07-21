import math # Importa todas as funções de math.

# Abaixo, cada linha importa apenas uma função de math.

from math import ceil # Arredonda pra cima
from math import floor # Arredonda pra baixo
from math import trunc # Trunca o número
from math import pow # Calcula a potência
from math import sqrt # Tira a raiz quadrada
from math import factorial # Fatorial de um número

# Se precisar de duas funções, coloque uma vírgula entre elas depois do "import".

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}.' .format(num, math.ceil(raiz))) # Caso você tenha importado toda a biblioteca math.
print('A raiz de {} é igual a {}.' .format(num, ceil(raiz))) # Caso você tenha importado apenas a função ceil.

import random # Para números randômicos.
num2 = random.random() # "randint" para gerar um número inteiro. Coloque números dentro do parentêses para criar um mínimo e um máximo de número gerados.
print(num2)

# import emoji # Para emojis. Para essa é necessário baixar.
# print(emoji.emojize('Olá, mundo :earth_americas:'), use_aliases=True)