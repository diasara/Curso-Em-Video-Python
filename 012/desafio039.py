#  Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Em que ano você nasceu? '))

idade = date.today().year - ano

if idade == 18:
	print('Está na hora exata de você se alistar!')
elif idade < 18:
	print('Ainda não está na hora de você se alistar.')
	print('Ainda falta {} anos.' .format(18 - idade))
else:
	print('Já passou da hora de você se alistar.')
	print('Você está {} anos atrasado' .format(abs(18 - idade)))
