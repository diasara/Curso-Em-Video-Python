# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
# foram necessários para vencer.

from random import randint

numero = randint(0, 5)
count = 0
chute = -1

while chute != numero:
	chute = int(input('Qual o seu chute? '))
	count += 1

if count == 1:
	print('Parabéns! Você acertou com uma única tentativa!')
else:
	print('Parabéns! Você acertou com {} tentativas!' .format(count))
