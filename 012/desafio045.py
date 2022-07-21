# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

print(''' O que você vai jogar?
	( 1 ) Pedra
	( 2 ) Papel
	( 3 ) Tesoura''')
usuario = int(input())

computador = randint(1,3)

if usuario == computador:
	print('EMPATE')
elif usuario == 1:
	if computador == 2:
		print('COMPUTADOR VENCEU!')
	if computador == 3:
		print('VOCÊ VENCEU!')
elif usuario == 2:
	if computador == 1:
		print('VOCÊ VENCEU!')
	if computador == 3:
		print('COMPUTADOR VENCEU!')
elif usuario == 3:
	if computador == 1:
		print('COMPUTADOR VENCEU!')
	if computador == 2:
		print('VOCÊ VENCEU!')

# Outro modo

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(1,3)

print(''' O que você vai jogar?
	( 1 ) Pedra
	( 2 ) Papel
	( 3 ) Tesoura''')
usuario = int(input())

if 0 < usuario < 4:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    
    print('-=' * 11)
    print('Computador jogou {}.' .format(itens[computador - 1]))
    print('Jogador jogou {}.' .format(itens[usuario - 1]))
    print('-=' * 11)


    if usuario == computador:
	    print('EMPATE')
    elif usuario == 1:
	    if computador == 2:
		    print('COMPUTADOR VENCEU!')
	    if computador == 3:
		    print('VOCÊ VENCEU!')
    elif usuario == 2:
	    if computador == 1:
		    print('VOCÊ VENCEU!')
	    if computador == 3:
		    print('COMPUTADOR VENCEU!')
    elif usuario == 3:
	    if computador == 1:
		    print('COMPUTADOR VENCEU!')
	    if computador == 2:
		    print('VOCÊ VENCEU!')
else:
    print('Opção inválida!')