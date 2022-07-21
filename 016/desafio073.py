#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na orde de colocação. Depois mostre:
#  A) Apenas os 5 primeiros colocados.
#  B) Os últimos 4 colocados da tabela.
#  C) Uma lista com os times em ordem alfabética.
#  D) Em que posição na tabela está o time da Chapecoense.

# Fiz a questão me baseando no campeonato de 2018 que é o ano do vídeo, pois atualmente a Chapecoense não tá na série A.

tabela = ('Palmeiras', 'Flamengo', 'Internacional',
          'Grêmio', 'São Paulo', 'Atlético - MG',
          'Athletico - PR', 'Cruzeiro', 'Botafogo',
          'Santos', 'Bahia', 'Fluminense', 'Corinthians',
          'Chapecoense', 'Ceará SC', 'Vasco da Gama',
          'Sport Recife', 'América - MG', 'EC Vitória', 'Paraná')

print('\nOs cinco primeiro colocados são:')
print(tabela[0:5])

print('\nOs últimos quatro colocados são:')
print(tabela[-4:])

print('\nOs times em ordem alfabética:')
print(sorted(tabela))

print(f'\nA Chapecoense está na posição {tabela.index("Chapecoense") + 1}.')
