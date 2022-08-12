# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.

# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
# informado corretamente.

def ficha(nome = '<desconhecido>', gols = '0'):
    if not gols.isnumeric():
        gols = 0

    print(f'O jogador se chama {nome} e fez {gols} gols no campeonato brasileiro.')

nome = str(input('Qual o nome do jogador? ')).title().strip()
gols = str(input('Quantos gols ele fez? ')) # Em string porque não dá pra converter nada em inteiro

if nome in '' and gols in '':
    ficha()
elif nome in '':
    ficha(gols = gols)
elif gols in '':
    ficha(nome = nome)
else:
    ficha(nome, gols)
